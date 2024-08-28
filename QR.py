import qrcode

upi_id=input("Enter your UPI ID = ")

phonepe_url= f'upi:pay?pa={upi_id}&pn=Recipent%20RATNA'
paytm_url= f'upi:pay?pa={upi_id}&pn=Recipent%20RATNA'
googlepay_url= f'upi:pay?pa={upi_id}&pn=Recipent%20RATNA'

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
googlepay_qr = qrcode.make(googlepay_url)

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
googlepay_qr.save('googlepay_qr.png')

phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()