## **The software**
You will test a webshop, which can be found here: https://grocerymate.masterschool.com/

The webshop has the following basic functionalities:

- Register and login functionality
- Searching for products, sorting on price, categories of products
- Add products to favorites
- Add products to basket
- Check-out process: billing and sending information in a form, choose payment method. Calculation of costs (calculate total price)

## **New features**

### **1. Product Rating System**

**Vague Requirement**:

- Users should be able to rate products with a 5-star system and have the option to add written feedback.

**Questions**:

1. Can users submit a star rating without writing a review, or is written feedback mandatory?
2. What happens if a user submits an empty review or selects zero stars?
3. Can a user edit or delete their own review after submission?
4. Are multiple reviews from the same user allowed on the same product?
5. Does the review system prevent spam or abuse (e.g., submitting the same review multiple times quickly)?

**Detailed Requirement**:

1. Users can rate a product on a scale of 1 to 5 stars and leave a written review.
2. Reviews must be submitted by logged-in users.
3. The system should prevent users from submitting a review with invalid or inappropriate content.
4. Users can only submit one review per product, but they can edit or delete their own reviews.
5. All reviews will be displayed on the product page with the newest at the top.
6. Reviews should be monitored for abuse (e.g., offensive language, spam).
7. A product’s overall rating is the average of all ratings submitted by users.


### **2. Age Verification for Alcoholic Products**

**Vague Requirement**:

- Alcoholic products require age verification. A modal should appear when navigating to the alcoholic products category asking if the user is 18+. Users must input their age before accessing the alcoholic products.
**Questions**:

1. Does the age verification modal appear every time a user navigates to alcoholic products, or only once per session?
2. What happens if the user enters an invalid or unrealistic age (e.g., 5 years old or 150 years old)?
3. Can users bypass the age verification check using browser tools or direct URLs?
4. If a user under 18 tries to purchase alcohol, does the system block them at checkout?
5. Is there a clear way for users who accidentally entered the wrong age to retry verification?

**Detailed Requirement**:

1. When a user navigates to the alcoholic products category, a modal should appear asking them to confirm they are 18+ years old.
2. The modal should prompt users to enter their date of birth (e.g., in MM/DD/YYYY format).
3. If the user is underage (e.g., under 18 years old), the system should block them from viewing alcoholic products and display an error message such as "You must be at least 18 years old to view alcoholic products."
4. Once a user has verified their age, the system should remember the decision for that session, or for the user’s next visit if they log in.
5. Users who refuse to provide age verification should be prevented from accessing the category.
6. The age verification process should be in compliance with local laws and regulations regarding alcohol sales.

### **3. Shipping Cost Changes**

**Vague Requirement**:

- Free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.

**Questions**:

1. Is free shipping applied correctly when the order total exceeds the required amount?
2. What happens if the order total fluctuates around the free shipping threshold due to adding/removing items?
3. Does applying a discount code that lowers the total below the threshold correctly remove free shipping?
4. Is the shipping cost (or free shipping) clearly displayed in the checkout process?
5. Does the system dynamically update the shipping cost as users modify their cart, or is a page refresh needed?

**Detailed Requirement**:

1. Free shipping is available for orders above a specified threshold (e.g., $50). Orders below this threshold will incur a shipping fee.
2. The system must display shipping costs dynamically during the checkout process and update them as the user adds or removes products.
3. If the user’s order total exceeds the free shipping threshold, free shipping should automatically be applied.
4. The system should clearly indicate the shipping cost in the cart and on the checkout page before the user confirms their order.
5. The user should also be informed when they are close to the free shipping threshold (e.g., "Add $10 more to your cart to qualify for free shipping").
6. International shipping rates, if applicable, should be calculated based on the user’s delivery address.