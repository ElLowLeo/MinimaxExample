#!/bin/bash

if ! python -c "import termcolor" &>/dev/null; then
    echo -e "\033[0;33m[ * ]\033[0m Termcolor is not installed. Installing..."
    pip install termcolor
fi

show_menu() {
    clear
    echo -e "\033[0;33m[ * ]\033[0m Choose a file to open:"
    echo -e "\033[0;33m( 1 )\033[0m minimaxExample.pt"
    echo -e "\033[0;33m( 2 )\033[0m minimaxExample.py"
}
show_menu

read -p "Enter your choice: " choice

case "$choice" in
    1)
        python highlighting.py
        ;;
    2)
        python MinimaxExampleCode/minimaxExample.py
        ;;
    *)
        echo -e "\033[0;31mInvalid choice. Please choose again.\033[0m"
    ;;
esac
