def displayInvoice(username, amount, dueDate):
    print(f"Hello {username}")
    print(f"Your bill of {amount:.2f} is due: {dueDate}")

displayInvoice("BroCode", 42.50, "01/01")