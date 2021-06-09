cat input.txt | python3 initialize.py > output.txt
diff output.txt expected_output.txt