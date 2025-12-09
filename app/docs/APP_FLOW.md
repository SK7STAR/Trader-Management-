# 📲 App Flow & Screen Structure – Trader Management APK

This document explains how the app works from the user’s point of view:
which screens exist, what each screen does, and how they connect.

---

## 1️⃣ Home Screen

**Name:** `HomeScreen`  

**Shows:**
- App title: **Trader Management**
- Premium status:
  - `Free User`  
  - or `Premium Active – X days left`
- Main buttons:
  - **Trade Entry & P&L**
  - **Risk Management**
  - **Premium Tools**
  - **Activate Premium**
  - **Settings / Help**

**Purpose:**  
Entry point of the app. From here, user navigates to all other tools.

---

## 2️⃣ Trade Entry & P&L Screen

**Name:** `TradeEntryScreen`  

**User inputs:**
- Entry price
- Stop Loss (SL)
- Take Profit (TP)
- Capital or Quantity
- Leverage

**App calculates:**
- Expected profit if TP hit
- Expected loss if SL hit
- Risk amount in ₹
- Risk-to-Reward (RR) ratio
- (Optional) Break-even level

**Purpose:**  
Quickly see if a trade is worth taking and how much can be gained/lost.

---

## 3️⃣ Risk Management Screen

**Name:** `RiskManagementScreen`  

**User inputs:**
- Account size (total capital)
- Risk % per trade (e.g. 1%, 2%)
- Entry price
- Stop Loss price

**App calculates:**
- Maximum allowed loss in ₹
- Recommended position size (quantity)
- Whether the trade is within safe risk limits

**Purpose:**  
Keeps the trader within safe risk rules and prevents over-leverage.

---

## 4️⃣ Premium Tools Screen

**Name:** `PremiumToolsScreen`  

**Access:**
- Locked for free users
- Fully available if premium is active

**Tools inside:**
- Advanced profit calculator:
  - Uses risk %, RR, entry, SL, TP, fees %
  - Shows net profit after fees
- Fees analysis:
  - Shows total exchange fees for a trade
- Future tools:
  - Capital growth calculator
  - Trade journal
  - Export history
  - Liquidity / stop-hunt helper

**Purpose:**  
Give serious traders deeper tools for planning and optimization.

---

## 5️⃣ Activate Premium Screen

**Name:** `ActivatePremiumScreen`  

**Shows:**
- Plan info: `₹50 / 30 days – Premium Access`
- What premium unlocks
- Button: **“Pay ₹50 & Unlock Premium”**

**Flow:**
1. User taps **Pay** button.
2. App calls backend `/create_order`.
3. App opens payment gateway.
4. After successful payment, backend activates premium.
5. App checks `/check_premium` and shows:
   - `Premium Active – valid till DD/MM/YYYY`.

**Purpose:**  
Simple, one-tap way to upgrade and unlock all premium tools.

---

## 6️⃣ Settings & Help Screen

**Name:** `SettingsScreen`  

**User can change:**
- Default risk % (e.g. 1%, 2%)
- Default fees % (exchange dependent)
- Default leverage (e.g. 10×)
- Theme:
  - Light / Dark
  - SK7•STAR Black & Gold (for premium users)

**Also shows:**
- Contact / support info (e.g. Telegram)
- App version info

**Purpose:**  
Allows user to personalize the app and get help when needed.

---

## 7️⃣ App Startup Logic (High Level)

When the app starts:

1. Load local data:
   - user_id  
   - last known premium state  
2. Call backend `/check_premium` with `user_id`.
3. If premium is active and not expired:
   - Show **Premium Active** on Home screen.
   - Unlock Premium Tools screen.
4. If premium is expired or never purchased:
   - Show **Free User**.
   - Lock Premium Tools and show upgrade option.

---

## Status

✅ App flow **planned and documented**  
⏳ UI and real code will be added in the next development phase.
