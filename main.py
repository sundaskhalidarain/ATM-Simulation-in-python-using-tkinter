import tkinter as tk

# =========================================================
# MAIN WINDOW
# =========================================================

window = tk.Tk()
window.title("ATM Banking")
window.geometry("400x500")
window.configure(bg="#F4F7FB")
window.resizable(False, False)

# =========================================================
# COLORS
# =========================================================

DARK_BLUE = "#102A43"
BLUE = "#1976D2"
LIGHT_BLUE = "#EAF3FF"
WHITE = "#FFFFFF"
GREEN = "#16A085"
RED = "#E74C3C"
GRAY = "#6B7280"

# =========================================================
# STARTING BALANCE
# =========================================================

s_bal = 10000

# =========================================================
# HEADER
# =========================================================

header = tk.Frame(
    window,
    bg=DARK_BLUE,
    height=90
)
header.pack(fill="x")

heading = tk.Label(
    header,
    text="🏦  ATM BANKING",
    font=("Arial", 22, "bold"),
    bg=DARK_BLUE,
    fg=WHITE
)
heading.pack(pady=25)

# =========================================================
# LOGIN CARD
# =========================================================

login_card = tk.Frame(
    window,
    bg=WHITE,
    padx=30,
    pady=30
)
login_card.pack(padx=35, pady=40, fill="x")

label = tk.Label(
    login_card,
    text="Welcome Back",
    font=("Arial", 20, "bold"),
    bg=WHITE,
    fg=DARK_BLUE
)
label.pack(pady=(0, 5))

sub_label = tk.Label(
    login_card,
    text="Enter your 4-digit PIN",
    font=("Arial", 11),
    bg=WHITE,
    fg=GRAY
)
sub_label.pack(pady=(0, 20))

# =========================================================
# PIN ENTRY
# =========================================================

pin_entry = tk.Entry(
    login_card,
    width=15,
    show="●",
    justify="center",
    font=("Arial", 18),
    bd=1,
    relief="solid"
)
pin_entry.pack(pady=10)

# =========================================================
# CHECK BALANCE WINDOW
# =========================================================

def check_bal():

    balance_window = tk.Toplevel(window)
    balance_window.title("Check Balance")
    balance_window.geometry("320x250")
    balance_window.configure(bg="#F4F7FB")
    balance_window.resizable(False, False)

    # Window title
    title = tk.Label(
        balance_window,
        text="💰 Account Balance",
        font=("Arial", 18, "bold"),
        bg=DARK_BLUE,
        fg=WHITE,
        pady=15
    )
    title.pack(fill="x")

    # Balance card
    balance_card = tk.Frame(
        balance_window,
        bg=LIGHT_BLUE,
        padx=20,
        pady=20
    )
    balance_card.pack(padx=30, pady=25, fill="x")

    balance_title = tk.Label(
        balance_card,
        text="AVAILABLE BALANCE",
        font=("Arial", 10, "bold"),
        bg=LIGHT_BLUE,
        fg=GRAY
    )
    balance_title.pack()

    show_balance = tk.Label(
        balance_card,
        text=f"Rs. {s_bal:,}",
        font=("Arial", 24, "bold"),
        bg=LIGHT_BLUE,
        fg=BLUE
    )
    show_balance.pack(pady=5)

# =========================================================
# WITHDRAW WINDOW
# =========================================================

def withdraw_money():

    withdraw_window = tk.Toplevel(window)
    withdraw_window.title("Withdraw Money")
    withdraw_window.geometry("350x350")
    withdraw_window.configure(bg="#F4F7FB")
    withdraw_window.resizable(False, False)

    # Header
    title = tk.Label(
        withdraw_window,
        text="💸 Withdraw Money",
        font=("Arial", 18, "bold"),
        bg=DARK_BLUE,
        fg=WHITE,
        pady=15
    )
    title.pack(fill="x")

    # Card
    withdraw_card = tk.Frame(
        withdraw_window,
        bg=WHITE,
        padx=25,
        pady=25
    )
    withdraw_card.pack(padx=30, pady=25, fill="x")

    withdraw_label = tk.Label(
        withdraw_card,
        text="Enter Withdrawal Amount",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=DARK_BLUE
    )
    withdraw_label.pack()

    wd_entry = tk.Entry(
        withdraw_card,
        font=("Arial", 14),
        justify="center"
    )
    wd_entry.pack(pady=12)

    def process_withdraw():

        global s_bal

        try:
            amount = int(wd_entry.get())

            if amount <= 0:
                result.config(
                    text="Enter a valid amount!",
                    fg=RED
                )

            elif amount <= s_bal:

                s_bal = s_bal - amount

                result.config(
                    text=f"✓ Withdrawal Successful\n"
                         f"Withdrawn: Rs. {amount:,}\n"
                         f"Remaining: Rs. {s_bal:,}",
                    fg=GREEN
                )

            else:

                result.config(
                    text="✕ Insufficient Balance!",
                    fg=RED
                )

        except ValueError:

            result.config(
                text="Please enter numbers only!",
                fg=RED
            )

    withdraw_button = tk.Button(
        withdraw_card,
        text="WITHDRAW",
        bg=BLUE,
        fg=WHITE,
        font=("Arial", 11, "bold"),
        bd=0,
        padx=25,
        pady=8,
        cursor="hand2",
        command=process_withdraw
    )
    withdraw_button.pack()

    result = tk.Label(
        withdraw_card,
        text="",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=GREEN
    )
    result.pack(pady=12)

# =========================================================
# DEPOSIT WINDOW
# =========================================================

def deposit_money():

    deposit_window = tk.Toplevel(window)
    deposit_window.title("Deposit Money")
    deposit_window.geometry("350x350")
    deposit_window.configure(bg="#F4F7FB")
    deposit_window.resizable(False, False)

    # Header
    title = tk.Label(
        deposit_window,
        text="💵 Deposit Money",
        font=("Arial", 18, "bold"),
        bg=DARK_BLUE,
        fg=WHITE,
        pady=15
    )
    title.pack(fill="x")

    # Card
    deposit_card = tk.Frame(
        deposit_window,
        bg=WHITE,
        padx=25,
        pady=25
    )
    deposit_card.pack(padx=30, pady=25, fill="x")

    deposit_label = tk.Label(
        deposit_card,
        text="Enter Deposit Amount",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=DARK_BLUE
    )
    deposit_label.pack()

    deposit_entry = tk.Entry(
        deposit_card,
        font=("Arial", 14),
        justify="center"
    )
    deposit_entry.pack(pady=12)

    def process_deposit():

        global s_bal

        try:
            amount = int(deposit_entry.get())

            if amount <= 0:

                result.config(
                    text="Enter a valid amount!",
                    fg=RED
                )

            else:

                s_bal = s_bal + amount

                result.config(
                    text=f"✓ Deposit Successful\n"
                         f"Deposited: Rs. {amount:,}\n"
                         f"New Balance: Rs. {s_bal:,}",
                    fg=GREEN
                )

        except ValueError:

            result.config(
                text="Please enter numbers only!",
                fg=RED
            )

    deposit_button = tk.Button(
        deposit_card,
        text="DEPOSIT",
        bg=GREEN,
        fg=WHITE,
        font=("Arial", 11, "bold"),
        bd=0,
        padx=25,
        pady=8,
        cursor="hand2",
        command=process_deposit
    )
    deposit_button.pack()

    result = tk.Label(
        deposit_card,
        text="",
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=GREEN
    )
    result.pack(pady=12)

# =========================================================
# ATM MENU
# =========================================================

def my_fun():

    pin = pin_entry.get()

    if pin == "0313":

        # Hide login screen
        header.pack_forget()
        login_card.pack_forget()

        # =================================================
        # ATM HEADER
        # =================================================

        menu_header = tk.Frame(
            window,
            bg=DARK_BLUE,
            pady=20
        )
        menu_header.pack(fill="x")

        menu_label = tk.Label(
            menu_header,
            text="ATM MENU",
            font=("Arial", 22, "bold"),
            bg=DARK_BLUE,
            fg=WHITE
        )
        menu_label.pack()

        welcome = tk.Label(
            menu_header,
            text="Select a transaction",
            font=("Arial", 10),
            bg=DARK_BLUE,
            fg="#B8C7D9"
        )
        welcome.pack()

        # =================================================
        # MENU CARD
        # =================================================

        menu_card = tk.Frame(
            window,
            bg=WHITE,
            padx=30,
            pady=25
        )
        menu_card.pack(padx=35, pady=30, fill="x")

        # =================================================
        # CHECK BALANCE BUTTON
        # =================================================

        check_button = tk.Button(
            menu_card,
            text="💰  CHECK BALANCE",
            font=("Arial", 12, "bold"),
            bg=LIGHT_BLUE,
            fg=BLUE,
            bd=0,
            padx=25,
            pady=8,
            cursor="hand2",
            command=check_bal
        )
        check_button.pack(pady=5)

        # =================================================
        # WITHDRAW BUTTON
        # =================================================

        withdraw_button = tk.Button(
            menu_card,
            text="💸  WITHDRAW",
            font=("Arial", 12, "bold"),
            bg=LIGHT_BLUE,
            fg=BLUE,
            bd=0,
            padx=25,
            pady=8,
            cursor="hand2",
            command=withdraw_money
        )
        withdraw_button.pack(pady=5)

        # =================================================
        # DEPOSIT BUTTON
        # =================================================

        deposit_button = tk.Button(
            menu_card,
            text="💵  DEPOSIT",
            font=("Arial", 12, "bold"),
            bg=LIGHT_BLUE,
            fg=BLUE,
            bd=0,
            padx=25,
            pady=8,
            cursor="hand2",
            command=deposit_money
        )
        deposit_button.pack(pady=5)

        # =================================================
        # EXIT BUTTON
        # =================================================

        exit_button = tk.Button(
            menu_card,
            text="🚪  EXIT",
            font=("Arial", 12, "bold"),
            bg="#FDECEC",
            fg=RED,
            bd=0,
            padx=25,
            pady=8,
            cursor="hand2",
            command=window.destroy
        )
        exit_button.pack(pady=5)

    else:

        wrong_label = tk.Label(
            login_card,
            text="✕ Incorrect PIN",
            font=("Arial", 11, "bold"),
            bg=WHITE,
            fg=RED
        )
        wrong_label.pack(pady=10)

# =========================================================
# LOGIN BUTTON
# =========================================================

login = tk.Button(
    login_card,
    text="LOGIN  →",
    bg=BLUE,
    fg=WHITE,
    font=("Arial", 13, "bold"),
    bd=0,
    padx=30,
    pady=10,
    cursor="hand2",
    command=my_fun
)
login.pack(pady=15)

# =========================================================
# RUN APPLICATION
# =========================================================

window.mainloop()