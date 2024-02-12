python -m coverage run -p tests/pyt/test_game.py
python -m coverage run -p tests/pyt/test_game_manager.py
python -m coverage combine
python -m coverage html
read -p "Press any key to continue" x