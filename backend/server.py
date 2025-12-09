"""
Backend API Structure for Trader Management App
================================================

This backend handles:
- Payment gateway integration
- Premium activation (30 days)
- Premium expiry checking
- User ID verification
- Order creation for payment
- Webhook handling for payment success
"""

# --------------------------------------------
# 1. Planned API Endpoints
# --------------------------------------------

"""
/create_order
    - Called by the app when user taps "Pay ₹50"
    - Backend creates a payment order using Razorpay/Cashfree
    - Returns: order_id, amount, payment_key_id
"""

"""
/payment_webhook
    - Payment gateway calls this after successful payment
    - Backend verifies payment signature
    - If valid: activate premium for 30 days
"""

"""
/check_premium
    - App calls this every time it opens
    - Backend returns:
        is_premium: True/False
        premium_expiry: date
"""

# --------------------------------------------
# 2. Planned Database Structure (Simple)
# --------------------------------------------

"""
users = {
    "user_id_123": {
        "is_premium": True,
        "premium_expiry": "2025-12-01 14:30:00",
        "last_payment_id": "pay_ABC123"
    }
}
"""

# --------------------------------------------
# 3. Premium Logic Flow
# --------------------------------------------

"""
- User taps Pay → app requests /create_order
- User pays → gateway calls /payment_webhook
- Backend verifies payment
- Backend adds +30 days premium
- App checks /check_premium → unlocks features
"""

# --------------------------------------------
# NOTE:
# Real backend code will be added later using FastAPI or Flask.
# Right now we are only planning the structure.
# --------------------------------------------
