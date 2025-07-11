import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import re

class ChessComBot:
    def __init__(self, headless=False):
        self.setup_driver(headless)
        self.board_state = self.init_board()
        self.white_to_move = True
        self.move_log = []
        self.game_active = False
        self.playing_as_white = True
        
        # Piece values for evaluation
        self.piece_values = {
            'K': 0, 'Q': 900, 'R': 500, 'B': 300, 'N': 300, 'P': 100,
            'k': 0, 'q': -900, 'r': -500, 'b': -300, 'n': -300, 'p': -100
        }
        
        # Chess.com square mapping
        self.files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.ranks = ['1', '2', '3', '4', '5', '6', '7', '8']

    def setup_driver(self, headless=False):
        """Setup Chrome WebDriver"""
        print("Setting up Chrome WebDriver...")
        
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        
        # Add options for better performance and compatibility
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Disable notifications
        prefs = {
            "profile.default_content_setting_values.notifications": 2
        }
        chrome_options.add_experimental_option("prefs", prefs)
        
        try:
            # Try to use system ChromeDriver first
            self.driver = webdriver.Chrome(options=chrome_options)
            self.wait = WebDriverWait(self.driver, 15)
            
            # Execute script to remove webdriver property
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            print("Chrome WebDriver setup successful!")
        except Exception as e:
            print(f"Error setting up WebDriver: {e}")
            print("Make sure you have ChromeDriver installed and in PATH")
            raise

    def init_board(self):
        """Initialize chess board"""
        return [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

    def navigate_to_chess_com(self):
        """Navigate to chess.com"""
        print("Navigating to chess.com...")
        self.driver.get("https://www.chess.com")
        time.sleep(5)

    def login_if_needed(self, username=None, password=None):
        """Handle login if credentials are provided"""
        if username and password:
            try:
                print("Attempting to login...")
                # Look for login button with more flexible selector
                login_selectors = [
                    "//a[contains(text(), 'Log In')]",
                    "//button[contains(text(), 'Log In')]",
                    "//a[@href='/login']",
                    ".login-button",
                    "#login-link"
                ]
                
                login_button = None
                for selector in login_selectors:
                    try:
                        if selector.startswith("//"):
                            login_button = self.wait.until(
                                EC.element_to_be_clickable((By.XPATH, selector))
                            )
                        else:
                            login_button = self.wait.until(
                                EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                            )
                        break
                    except TimeoutException:
                        continue
                
                if not login_button:
                    print("Could not find login button")
                    return False
                
                login_button.click()
                time.sleep(2)
                
                # Enter username with multiple possible selectors
                username_selectors = ["#username", "[name='username']", "[type='email']"]
                username_field = None
                
                for selector in username_selectors:
                    try:
                        username_field = self.wait.until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                        )
                        break
                    except TimeoutException:
                        continue
                
                if not username_field:
                    print("Could not find username field")
                    return False
                
                username_field.clear()
                username_field.send_keys(username)
                
                # Enter password
                password_selectors = ["#password", "[name='password']", "[type='password']"]
                password_field = None
                
                for selector in password_selectors:
                    try:
                        password_field = self.driver.find_element(By.CSS_SELECTOR, selector)
                        break
                    except NoSuchElementException:
                        continue
                
                if not password_field:
                    print("Could not find password field")
                    return False
                
                password_field.clear()
                password_field.send_keys(password)
                
                # Click login button
                login_submit_selectors = ["#login", "[type='submit']", ".login-button"]
                login_submit = None
                
                for selector in login_submit_selectors:
                    try:
                        login_submit = self.driver.find_element(By.CSS_SELECTOR, selector)
                        break
                    except NoSuchElementException:
                        continue
                
                if not login_submit:
                    print("Could not find login submit button")
                    return False
                
                login_submit.click()
                time.sleep(5)
                print("Login successful!")
                return True
                
            except Exception as e:
                print(f"Login failed: {e}")
                return False
        
        return True

    def start_game(self, game_type="blitz"):
        """Start a new game"""
        print(f"Starting {game_type} game...")
        
        try:
            # Look for Play button with multiple selectors
            play_selectors = [
                "//a[contains(@href, '/play')]",
                "//button[contains(text(), 'Play')]",
                ".play-button",
                "#play-button"
            ]
            
            play_button = None
            for selector in play_selectors:
                try:
                    if selector.startswith("//"):
                        play_button = self.wait.until(
                            EC.element_to_be_clickable((By.XPATH, selector))
                        )
                    else:
                        play_button = self.wait.until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                    break
                except TimeoutException:
                    continue
            
            if not play_button:
                print("Could not find play button")
                return False
            
            play_button.click()
            time.sleep(3)
            
            # Select game type with more flexible selectors
            game_selectors = {
                "blitz": ["//button[contains(text(), 'Blitz')]", ".blitz-button"],
                "rapid": ["//button[contains(text(), 'Rapid')]", ".rapid-button"],
                "bullet": ["//button[contains(text(), 'Bullet')]", ".bullet-button"]
            }
            
            game_button = None
            for selector in game_selectors.get(game_type, game_selectors["blitz"]):
                try:
                    if selector.startswith("//"):
                        game_button = self.wait.until(
                            EC.element_to_be_clickable((By.XPATH, selector))
                        )
                    else:
                        game_button = self.wait.until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                    break
                except TimeoutException:
                    continue
            
            if game_button:
                game_button.click()
                time.sleep(2)
            
            # Click play to find opponent
            play_now_selectors = [
                "//button[contains(text(), 'Play')]",
                ".play-now-button",
                "#play-now"
            ]
            
            play_now = None
            for selector in play_now_selectors:
                try:
                    if selector.startswith("//"):
                        play_now = self.wait.until(
                            EC.element_to_be_clickable((By.XPATH, selector))
                        )
                    else:
                        play_now = self.wait.until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                    break
                except TimeoutException:
                    continue
            
            if not play_now:
                print("Could not find play now button")
                return False
            
            play_now.click()
            print("Searching for opponent...")
            
            # Wait for game to start
            return self.wait_for_game_start()
            
        except Exception as e:
            print(f"Error starting game: {e}")
            return False

    def wait_for_game_start(self):
        """Wait for the game to begin"""
        print("Waiting for game to start...")
        
        try:
            # Wait for the chess board to appear with multiple selectors
            board_selectors = [".board", "#board", ".game-board", "[class*='board']"]
            
            board = None
            for selector in board_selectors:
                try:
                    board = WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    break
                except TimeoutException:
                    continue
            
            if not board:
                print("Could not find chess board")
                return False
            
            # Wait a bit more for the game to fully load
            time.sleep(5)
            
            # Determine if we're playing as white or black
            self.determine_player_color()
            
            self.game_active = True
            print("Game started!")
            return True
            
        except Exception as e:
            print(f"Game didn't start: {e}")
            self.game_active = False
            return False

    def determine_player_color(self):
        """Determine if we're playing as white or black"""
        try:
            # Check if the board is flipped (we're black)
            # Look for rank labels to determine orientation
            rank_labels = self.driver.find_elements(By.CSS_SELECTOR, ".coordinate-light, .coordinate-dark")
            
            if rank_labels:
                # Check if we can see '1' at the bottom
                bottom_coords = [label.text for label in rank_labels[-4:]]  # Get last few coordinates
                self.playing_as_white = '1' in bottom_coords
            else:
                # Alternative method: check board classes
                board_element = self.driver.find_element(By.CSS_SELECTOR, ".board, #board")
                board_classes = board_element.get_attribute("class")
                self.playing_as_white = "flipped" not in board_classes.lower()
                
            print(f"Playing as {'White' if self.playing_as_white else 'Black'}")
            
        except Exception as e:
            print(f"Could not determine player color: {e}")
            self.playing_as_white = True

    def is_our_turn(self):
        """Check if it's our turn to move"""
        try:
            # Multiple methods to check turn
            
            # Method 1: Check for active clock
            clock_selectors = [
                ".clock-playerTurn",
                ".clock.active",
                "[class*='clock'][class*='active']"
            ]
            
            for selector in clock_selectors:
                turn_indicators = self.driver.find_elements(By.CSS_SELECTOR, selector)
                if turn_indicators:
                    for indicator in turn_indicators:
                        indicator_classes = indicator.get_attribute("class")
                        if "bottom" in indicator_classes:
                            return self.playing_as_white
                        elif "top" in indicator_classes:
                            return not self.playing_as_white
            
            # Method 2: Check for move highlight or turn indicator
            turn_classes = [
                ".to-move",
                ".player-turn",
                "[class*='turn'][class*='white']",
                "[class*='turn'][class*='black']"
            ]
            
            for selector in turn_classes:
                elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                if elements:
                    for element in elements:
                        classes = element.get_attribute("class")
                        if "white" in classes:
                            return self.playing_as_white
                        elif "black" in classes:
                            return not self.playing_as_white
            
            # Default to checking if any pieces are draggable
            our_pieces = self.driver.find_elements(By.CSS_SELECTOR, ".piece[draggable='true']")
            return len(our_pieces) > 0
            
        except Exception as e:
            print(f"Error checking turn: {e}")
            return False

    def get_board_state(self):
        """Get current board state from chess.com"""
        try:
            # Find all pieces on the board
            piece_selectors = [
                ".piece",
                "[class*='piece']",
                ".square .piece"
            ]
            
            pieces = []
            for selector in piece_selectors:
                pieces = self.driver.find_elements(By.CSS_SELECTOR, selector)
                if pieces:
                    break
            
            if not pieces:
                print("No pieces found on board")
                return self.board_state
            
            # Reset board
            board = [['.' for _ in range(8)] for _ in range(8)]
            
            for piece in pieces:
                try:
                    # Get piece position and type from CSS classes or attributes
                    class_list = piece.get_attribute("class").split()
                    
                    piece_type = None
                    position = None
                    
                    for cls in class_list:
                        if cls.startswith("square-"):
                            position = cls.replace("square-", "")
                        elif cls in ['wp', 'bp', 'wr', 'br', 'wn', 'bn', 'wb', 'bb', 'wq', 'bq', 'wk', 'bk']:
                            piece_type = cls
                        elif cls.startswith("piece-"):
                            piece_type = cls.replace("piece-", "")
                    
                    # Alternative method: check parent square
                    if not position:
                        parent = piece.find_element(By.XPATH, "..")
                        parent_classes = parent.get_attribute("class").split()
                        for cls in parent_classes:
                            if cls.startswith("square-"):
                                position = cls.replace("square-", "")
                                break
                    
                    if piece_type and position and len(position) == 2:
                        file = ord(position[0]) - ord('a')
                        rank = 8 - int(position[1])
                        
                        if 0 <= file < 8 and 0 <= rank < 8:
                            # Convert to our notation
                            if piece_type.startswith('w'):
                                board[rank][file] = piece_type[1].upper()
                            else:
                                board[rank][file] = piece_type[1].lower()
                
                except Exception as e:
                    continue
            
            return board
            
        except Exception as e:
            print(f"Error getting board state: {e}")
            return self.board_state

    def make_move_on_board(self, from_square, to_square):
        """Make a move on the chess.com board"""
        try:
            print(f"Making move: {from_square} -> {to_square}")
            
            # Find the piece to move with multiple selectors
            from_selectors = [
                f".square-{from_square}",
                f"[class*='square-{from_square}']",
                f"[data-square='{from_square}']"
            ]
            
            from_element = None
            for selector in from_selectors:
                try:
                    from_element = self.driver.find_element(By.CSS_SELECTOR, selector)
                    break
                except NoSuchElementException:
                    continue
            
            if not from_element:
                print(f"Could not find source square: {from_square}")
                return False
            
            # Find the destination square
            to_selectors = [
                f".square-{to_square}",
                f"[class*='square-{to_square}']",
                f"[data-square='{to_square}']"
            ]
            
            to_element = None
            for selector in to_selectors:
                try:
                    to_element = self.driver.find_element(By.CSS_SELECTOR, selector)
                    break
                except NoSuchElementException:
                    continue
            
            if not to_element:
                print(f"Could not find destination square: {to_square}")
                return False
            
            # Try multiple methods to make the move
            actions = ActionChains(self.driver)
            
            # Method 1: Click and drag
            try:
                actions.click_and_hold(from_element).move_to_element(to_element).release().perform()
                time.sleep(1)
                return True
            except Exception as e:
                print(f"Click and drag failed: {e}")
            
            # Method 2: Drag and drop
            try:
                actions.drag_and_drop(from_element, to_element).perform()
                time.sleep(1)
                return True
            except Exception as e:
                print(f"Drag and drop failed: {e}")
            
            # Method 3: Click from then click to
            try:
                from_element.click()
                time.sleep(0.5)
                to_element.click()
                time.sleep(1)
                return True
            except Exception as e:
                print(f"Click method failed: {e}")
            
            return False
            
        except Exception as e:
            print(f"Error making move: {e}")
            return False

    def calculate_best_move(self, board):
        """Calculate the best move using simple evaluation"""
        valid_moves = self.get_valid_moves(board)
        
        if not valid_moves:
            return None
        
        # Simple evaluation - prefer captures and center control
        best_move = None
        best_score = float('-inf') if self.playing_as_white else float('inf')
        
        for move in valid_moves:
            score = self.evaluate_move(board, move)
            
            if self.playing_as_white and score > best_score:
                best_score = score
                best_move = move
            elif not self.playing_as_white and score < best_score:
                best_score = score
                best_move = move
        
        return best_move

    def get_valid_moves(self, board):
        """Get all valid moves for current position"""
        moves = []
        
        for rank in range(8):
            for file in range(8):
                piece = board[rank][file]
                
                if piece == '.':
                    continue
                
                # Check if it's our piece
                is_white_piece = piece.isupper()
                if is_white_piece != self.playing_as_white:
                    continue
                
                # Generate moves for this piece
                piece_moves = self.get_piece_moves(board, rank, file, piece.lower())
                moves.extend(piece_moves)
        
        return moves

    def get_piece_moves(self, board, rank, file, piece_type):
        """Get moves for a specific piece"""
        moves = []
        
        if piece_type == 'p':
            moves.extend(self.get_pawn_moves(board, rank, file))
        elif piece_type == 'r':
            moves.extend(self.get_rook_moves(board, rank, file))
        elif piece_type == 'n':
            moves.extend(self.get_knight_moves(board, rank, file))
        elif piece_type == 'b':
            moves.extend(self.get_bishop_moves(board, rank, file))
        elif piece_type == 'q':
            moves.extend(self.get_queen_moves(board, rank, file))
        elif piece_type == 'k':
            moves.extend(self.get_king_moves(board, rank, file))
        
        return moves

    def get_pawn_moves(self, board, rank, file):
        """Get pawn moves"""
        moves = []
        is_white = board[rank][file].isupper()
        direction = -1 if is_white else 1
        start_rank = 6 if is_white else 1
        
        # Forward move
        new_rank = rank + direction
        if 0 <= new_rank < 8 and board[new_rank][file] == '.':
            moves.append((rank, file, new_rank, file))
            
            # Double move from starting position
            if rank == start_rank and new_rank + direction < 8 and board[new_rank + direction][file] == '.':
                moves.append((rank, file, new_rank + direction, file))
        
        # Captures
        for df in [-1, 1]:
            new_file = file + df
            if 0 <= new_file < 8 and 0 <= new_rank < 8:
                target = board[new_rank][new_file]
                if target != '.' and target.isupper() != is_white:
                    moves.append((rank, file, new_rank, new_file))
        
        return moves

    def get_rook_moves(self, board, rank, file):
        """Get rook moves"""
        moves = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for dr, df in directions:
            for i in range(1, 8):
                new_rank = rank + dr * i
                new_file = file + df * i
                
                if not (0 <= new_rank < 8 and 0 <= new_file < 8):
                    break
                
                target = board[new_rank][new_file]
                if target == '.':
                    moves.append((rank, file, new_rank, new_file))
                else:
                    # Can capture enemy piece
                    if target.isupper() != board[rank][file].isupper():
                        moves.append((rank, file, new_rank, new_file))
                    break
        
        return moves

    def get_knight_moves(self, board, rank, file):
        """Get knight moves"""
        moves = []
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), 
                       (1, -2), (1, 2), (2, -1), (2, 1)]
        
        for dr, df in knight_moves:
            new_rank = rank + dr
            new_file = file + df
            
            if 0 <= new_rank < 8 and 0 <= new_file < 8:
                target = board[new_rank][new_file]
                if target == '.' or target.isupper() != board[rank][file].isupper():
                    moves.append((rank, file, new_rank, new_file))
        
        return moves

    def get_bishop_moves(self, board, rank, file):
        """Get bishop moves"""
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for dr, df in directions:
            for i in range(1, 8):
                new_rank = rank + dr * i
                new_file = file + df * i
                
                if not (0 <= new_rank < 8 and 0 <= new_file < 8):
                    break
                
                target = board[new_rank][new_file]
                if target == '.':
                    moves.append((rank, file, new_rank, new_file))
                else:
                    if target.isupper() != board[rank][file].isupper():
                        moves.append((rank, file, new_rank, new_file))
                    break
        
        return moves

    def get_queen_moves(self, board, rank, file):
        """Get queen moves"""
        moves = []
        moves.extend(self.get_rook_moves(board, rank, file))
        moves.extend(self.get_bishop_moves(board, rank, file))
        return moves

    def get_king_moves(self, board, rank, file):
        """Get king moves"""
        moves = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), 
                     (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for dr, df in directions:
            new_rank = rank + dr
            new_file = file + df
            
            if 0 <= new_rank < 8 and 0 <= new_file < 8:
                target = board[new_rank][new_file]
                if target == '.' or target.isupper() != board[rank][file].isupper():
                    moves.append((rank, file, new_rank, new_file))
        
        return moves

    def evaluate_move(self, board, move):
        """Evaluate a move"""
        from_rank, from_file, to_rank, to_file = move
        score = 0
        
        # Capture bonus
        target = board[to_rank][to_file]
        if target != '.':
            piece_value = self.piece_values.get(target, 0)
            score += abs(piece_value)
        
        # Center control bonus
        if 2 <= to_rank <= 5 and 2 <= to_file <= 5:
            score += 30
        
        # Piece development bonus
        if board[from_rank][from_file].lower() in ['n', 'b']:
            if (self.playing_as_white and from_rank == 7) or (not self.playing_as_white and from_rank == 0):
                score += 20
        
        # Add some randomness to avoid predictable play
        score += random.randint(-10, 10)
        
        return score

    def square_to_notation(self, rank, file):
        """Convert rank/file to chess notation"""
        return f"{chr(ord('a') + file)}{8 - rank}"

    def play_game(self):
        """Main game loop"""
        print("Starting game loop...")
        move_count = 0
        max_moves = 100  # Prevent infinite loops
        
        while self.game_active and move_count < max_moves:
            try:
                # Check if game is still active
                if not self.is_game_active():
                    print("Game ended!")
                    break
                
                # Check if it's our turn
                if not self.is_our_turn():
                    print("Waiting for opponent...")
                    time.sleep(2)
                    continue
                
                print(f"Move {move_count + 1}: It's our turn!")
                
                # Get current board state
                board = self.get_board_state()
                
                # Calculate best move
                best_move = self.calculate_best_move(board)
                
                if best_move:
                    from_rank, from_file, to_rank, to_file = best_move
                    from_square = self.square_to_notation(from_rank, from_file)
                    to_square = self.square_to_notation(to_rank, to_file)
                    
                    # Make the move
                    if self.make_move_on_board(from_square, to_square):
                        print(f"Move made: {from_square} -> {to_square}")
                        move_count += 1
                        time.sleep(3)  # Wait for move to register
                    else:
                        print("Failed to make move, trying again...")
                        time.sleep(2)
                else:
                    print("No valid moves found")
                    time.sleep(2)
                
            except Exception as e:
                print(f"Error in game loop: {e}")
                time.sleep(3)
        
        print("Game loop ended")

    def is_game_active(self):
        """Check if the game is still active"""
        try:
            # Look for game over indicators
            game_over_selectors = [
                ".game-over-modal",
                ".modal-game-over",
                ".game-over",
                "[class*='game-over']"
            ]
            
            for selector in game_over_selectors:
                game_over_elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                if game_over_elements:
                    return False
            
            # Check if board is still present
            board_selectors = [".board", "#board", ".game-board"]
            for selector in board_selectors:
                board = self.driver.find_elements(By.CSS_SELECTOR, selector)
                if board:
                    return True
            
            return False
            
        except Exception as e:
            print(f"Error checking game state: {e}")
            return False

    def close(self):
        """Close the browser"""
        if hasattr(self, 'driver'):
            self.driver.quit()
            print("Browser closed")


def main():
    """Main function to run the chess bot"""
    print("Chess.com Auto-Player Bot")
    print("=" * 40)
    
    # Configuration
    USERNAME = 'AhmadSheikh788'  # Set your chess.com username
    PASSWORD = '7seasahmad'  # Set your chess.
    GAME_TYPE = "blitz"  # "bullet", "blitz", or "rapid"
    HEADLESS = False  # Set to True to run without GUI
    
    bot = None
    
    try:
        # Create bot instance
        bot = ChessComBot(headless=HEADLESS)
        
        # Navigate to chess.com
        bot.navigate_to_chess_com()
        
        # Login if credentials provided
        if USERNAME and PASSWORD:
            bot.login_if_needed(USERNAME, PASSWORD)
        
        # Start a game
        if bot.start_game(GAME_TYPE):
            # Play the game
            bot.play_game()
        else:
            print("Failed to start game")
        
        # Keep browser open for a bit to see results
        time.sleep(10)
        
    except KeyboardInterrupt:
        print("\nBot stopped by user")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if bot:
            bot.close()




if __name__ == "__main__":
    main()