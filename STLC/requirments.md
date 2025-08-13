## **The software**
I will test a webshop, which can be found here: https://grocerymate.masterschool.com/

The webshop has the following basic functionalities:

- Register and login functionality
- Searching for products, sorting on price, categories of products
- Add products to favorites
- Add products to basket
- Check-out process: billing and sending information in a form, choose payment method. Calculation of costs (calculate total price)

## **New features**

### **Feature 1: Product Rating System**

## **Requirement:**

- Users should be able to rate products with a 5-star system and have the option to add written feedback.

**Questions**:
1. Can all users rate products or only those who have purchased the product?
2. Can a user rate the same product multiple times?
3. Will ratings appear instantly or only after admin approval?
4. Will there be a character limit for the written feedback (e.g. 200 characters)?

**Detailed Requirement**:

1. Only users who have purchased the product can submit a rating or review.
2. Users can rate a product on a scale of 1 to 5 stars and leave a written review.
3. Users can also leave optional written feedback with a maximum of 200 characters.
4. The system should prevent users from submitting a review with invalid or inappropriate content.
5. Users can only submit one review per product but they can edit or delete their own reviews.

### **Feature 2: Age Verification for Alcoholic Products**

**Requirement**:

- Alcoholic products require age verification. An age verification prompt should appear when navigating to the alcoholic products category asking if the user is 18+. Users must input their age before accessing the alcoholic products.

**Questions**:

1. Does the age verification prompt appear every time when a user navigates to alcoholic products or only once per session?
2. What happens if the user enters an invalid or unrealistic age (e.g. 5 years old or 150 years old)?
3. If a user under 18 tries to purchase alcohol does the system block them at checkout?
4. Will the process work identically on both mobile and desktop?

**Detailed Requirement**:

1. When a user navigates to the alcoholic products category, a promt should appear asking them to confirm they are 18+ years old.
2. The users to enter their date of birth in DD-MM-YYYY format.
3. If the user is underage (e.g. under 18 years old), the system should block them from viewing alcoholic products and display an error message such as "You must be at least 18 years old to view alcoholic products."
4. Once a user has verified their age, the system should remember the decision for that session or for the user’s next visit if they log in.
5. The feature must be fully functional on both desktop and mobile platforms.


### **Feature 3: Shipping Cost Changes**

**Requirement**:

- Free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.

**Questions**:

1. What is the exact threshold amount for free shipping?
2. Is the shipping fee the same for all locations or does it vary?
3. Is the free shipping threshold calculated based on the order total before or after discounts are applied?
4. If multiple shipping options (e.g. standard, express) are available and how is free shipping applied?

**Detailed Requirement**:

1. Orders with a final total (after discounts are applied) of $50 or more will receive free standard shipping.
2. Orders with a total below $50 will incur a $4.99 standard shipping fee.
3. Express delivery will always incur a charge, regardless of order value.
4. Location-based shipping fees will apply only for international orders.
