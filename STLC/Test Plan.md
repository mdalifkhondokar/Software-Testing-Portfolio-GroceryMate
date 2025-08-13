# **Test Plan for Social Media Platform Enhancements**

## **1. Analyze the Product – GroceryMate**

### **Objective**

The primary objective of this release is to enhance the GroceryMate webshop by introducing three new 
features and ensuring that all existing functionalities continue to operate smoothly without regression 
issues.

### **User Base**

The product is targeted at a wide range of users, including:

- new and returning online shoppers
- Age 18+ users (especially for alcohol category)
- Budget-conscious users comparing prices and shipping costs
- Tech-savvy and mobile-first users
- Logged-in users for personalized features (favorites, reviews, etc.)

### **Hardware and Software Specifications**

- **Hardware Requirements:**
    - Devices: Smartphones, tablets, laptops, desktop computers
    - Specifications: 
      - Standard configurations for Android and iOS devices, 
      - Minimum 4GB RAM and dual-core processor for desktops/laptops
- **Software Requirements:**
    - Operating Systems:
      - Mobile: Android 8+, iOS 12+
      - Desktop: Windows, macOS, Android, iOS
    - Supported Browsers: 
      - Google Chrome
      - Mozilla Firefox
      - Safari (for iOS and macOS)
      - Microsoft Edge

### **Product Functionality**

The new features introduced in this release are:

1. **Product Rating System** – Users can rate purchased products (1–5 stars, including half-stars) and leave written feedback.

2. **Age Verification Prompt for Alcoholic Products** – A prompt ensures that only users aged 18+ can view alcoholic products.

3. **Shipping Cost Changes** – Orders of $50 or more (after discounts) receive free standard shipping; others incur a $4.99 fee.


## **2. Design the Test Strategy – GroceryMate**

### **Scope of Testing**

- **In Scope:**

    - Product rating submission, validation and display
    - Age verification prompt flow for alcoholic products
    - Shipping cost calculation logic and display in checkout
    - Regression testing of existing checkout and basket functionality

- **Out of Scope:**
    - Backend database performance tuning
    - Third-party analytics tools
    - Payment gateway integration testing beyond existing flows

### **Type of Testing**

- Functional Testing – Verifying core features: add, edit, delete items and UI functionality.
- Regression Testing – Ensuring newly added changes don’t break existing features.
- Performance Testing – Checking for performance degradation with a large number of list items.
- Usability Testing – Validating that the interface is intuitive, simple, and user-friendly.
- Boundary Value Analysis 


### **Risks and Issues**

- **Risk:** Incorrect age verification logic could allow underage access.
- **Mitigation:** Thorough negative testing and boundary testing for age calculation.
- **Risk:** Shipping cost miscalculation affecting pricing.
- **Mitigation:** Test with varied order totals and discount combinations.
- **Risk:** Rating system spam or abuse.
- **Mitigation:** Ensure ratings are limited to verified purchases.


### **Test Logistics**

- **Patrick Bauer** - Test Manager
- **Md Alif Khondokar** - QA Engineer (Functional and Regression Testing)
- **Maria L** - QA Engineer (Performance and Security Testing)
- **Ronny** - QA Engineer (Usability Testing)
- **Maria Garcia** - Boundary Value Analysis 

## **3. Define Test Objectives – GroceryMate**

### **Objectives**

- **Functionality:** Ensure that users can add, edit, delete and manage grocery items as intended.
- **Performance:** Confirm that the application handles a large number of items without lag or errors.
- **Security:** Identify and mitigate potential security vulnerabilities.
- **Usability:** Assess whether users can intuitively interact with the platform without guidance.
- **Compatibility:** Ensure the application works smoothly across major browsers and screen sizes.

### **Expected Outcomes**

- **Functionality:** All core list management features operate reliably and without bugs.
- **Performance:** The app remains fast and responsive even with large item lists.
- **Security:** No significant vulnerabilities are detected.
- **Usability:** Users can perform tasks easily without confusion or error
- **Compatibility:** The app functions correctly on Chrome, Firefox, Safari and Edge across mobile and desktop.

## **4. Define Test Criteria – GroceryMate**

### **Suspension Criteria**

- Testing will be suspended if critical defects block further execution.
- Unavailable test environment or incomplete feature deployment.

- Testing will be suspended if critical defects are discovered that prevent further testing of core features (e.g., adding or managing grocery items).
- Testing will also be suspended in the event of:
    - Major application crashes or data loss
    - Inaccessibility of the test environment
    - Lack of required resources (testers, tools, devices)

### **Exit Criteria**

- All planned test cases have been created, reviewed, and executed.
- Run Rate: At least 95% of all test cases have been executed.
- Pass Rate: At least 90% of executed test cases have passed.
- All high and critical severity defects fixed and retested.
- No open severity 1 or 2 issues at release.

## **5. Resource Planning – GroceryMate**

- **Human Resources:** 
  - **QA team:** Test Manager, Functional QA Engineers, Usability and Performance Engineers
  - **Development team:** Developers for bug fixes and feature verification
  - **End users for UAT:** Developers for bug fixes and feature verification
- **Hardware:** 
  - PCs and laptops (Windows/macOS for desktop testing)
  - Smartphones and tablets (Android and iOS for mobile testing)
- **Software:** 
  - Browsers: Chrome, Firefox, Safari, Edge
  - Operating Systems: Windows, macOS, Android, iOS.
- **Infrastructure:** 
  - Staging environment with production-like setup.

## **6. Plan Test Environment**

**Environments:**

- DEV (Developer testing)
- TEST (QA functional and regression testing)
- ACC (User Acceptance Testing)
- PROD (Production release)

**Test Data:**

- Valid and invalid user accounts
- Purchased and non-purchased products
- Order totals near the $50 free shipping threshold

## **7. Schedule and Estimation**


| Activity            | Start Date | End Date   | Environment | Responsible Person | Estimated Effort |
| ------------------- | ---------- | ---------- | ----------- | ------------------ | ---------------- |
| Test Planning       | 20/08/2025 | 21/08/2025 | All         | QA Lead            | 8 hours          |
| Test Case Design    | 22/08/2025 | 25/08/2025 | All         | QA Team            | 16 hours         |
| Unit Testing        | 26/08/2025 | 27/08/2025 | DEV         | Developers         | 8 hours          |
| Integration Testing | 28/08/2025 | 29/08/2025 | TEST        | QA Team            | 8 hours          |
| System Testing      | 01/09/2025 | 03/09/2025 | TEST        | QA Team            | 12 hours         |
| Regression Testing  | 04/09/2025 | 05/09/2025 | TEST        | QA Team            | 8 hours          |
| UAT                 | 06/09/2025 | 07/09/2025 | ACC         | End Users          | 8 hours          |
| Production Release  | 08/09/2025 | 08/09/2025 | PROD        | DevOps             | 4 hours          |


## **8. Determine Test Deliverables**

Documents/tools that must be created to support testing activities in the project:

- **Test Plan Document** – Detailing the scope, strategy, and execution plan for testing.
- **Test Cases and Test Scripts** – Detailed test cases covering all functionalities, including edge cases and scenarios.
- **Test Data** – Data required to validate the various scenarios and test conditions (e.g., grocery items, categories).
- **Test Reports** – Reports summarizing test execution results, pass/fail rates and overall status.
- **Defect Reports** – Detailed logs of defects found during testing, including severity, reproduction steps and resolutions.
- **UAT Sign-off Document** – Formal sign-off from stakeholders confirming that the product meets business requirements and is ready for production.