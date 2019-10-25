def rearrangeMap(send, sold):
    send_values = list(send.values())
    sold_values = list(sold.values())

    send_values.sort()
    sold_values.sort()

    keys = send.keys()
    for key in keys:
        send[key] = send_values.pop(0)
        sold[key] = sold_values.pop(0)

send = { 'key_1': 10, 'key_2': 20 }
sold = { 'key_1': 20, 'key_2': 10 }

rearrangeMap(send, sold)

print(send)
print(sold)
