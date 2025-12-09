🧾 Payment & Premium Flow – Trader Management APK

This document explains how payment, premium activation, and expiry work in the Trader Management app.


---

1️⃣ Premium Plan Rules

Price: ₹50 per month

Access duration: 30 days from successful payment

After 30 days → premium automatically expires

Activation is automatic after payment (no manual code)

Payment is handled using a payment gateway (e.g. Razorpay / Cashfree)



---

2️⃣ Main Components

1. App (APK)

Shows “Pay ₹50 & Unlock Premium” button

Calls backend to create payment order

Checks premium status from backend

Unlocks/locks premium tools based on backend response



2. Backend Server

Talks to the payment gateway

Stores premium status and expiry

Exposes APIs like /create_order, /payment_webhook, /check_premium



3. Payment Gateway

Handles UPI / card / wallet payments

Sends a webhook to backend on payment success





---

3️⃣ User Flow – Step by Step

1. User opens app and goes to Activate Premium screen.


2. App shows plan: ₹50 / 30 days and a button:
“Pay ₹50 & Unlock Premium”


3. When user taps the button, the app calls backend:

Endpoint: /create_order

Sends: user_id



4. Backend creates a payment order with the gateway and returns:

order_id

amount

public_key (for gateway)



5. App opens the payment gateway checkout (UPI / card / wallet).


6. User completes payment.


7. Payment gateway marks the payment as successful and sends a webhook to backend (/payment_webhook).


8. Backend verifies the payment signature and if valid:

Finds the user_id linked to that order_id

Sets:

is_premium = true

premium_expiry = now + 30 days




9. Next time app calls /check_premium with user_id, backend replies:

is_premium = true

premium_expiry = <date>



10. App unlocks all premium tools and shows:

“Premium active – valid till DD/MM/YYYY”





---

4️⃣ Premium Check Logic

Every time the app starts (or opens Premium screen):

1. App sends user_id → /check_premium


2. Backend checks:

If is_premium is False → user is free

If is_premium is True but now > premium_expiry →

Set is_premium = False

User becomes free again




3. Backend returns final status:

Active premium with expiry date

OR free user (expired or never bought)




App uses this response to decide which features are unlocked.


---

5️⃣ Data Stored Per User (Backend Side)

For each user, backend stores for example:

user_id

is_premium (True / False)

premium_expiry (datetime)

last_payment_id (from gateway)



---

6️⃣ Why This System Is Good

No manual code sharing

Premium unlocks instantly after payment

Auto expiry after 30 days

Works clean with mobile app + backend + gateway

Easy to extend in the future (logs, invoices, etc.)



---

Status

✅ Payment flow planned
⏳ Implementation will be added in future backend development phase.
