# Schema Description (for RDBMS)

The following schema is proposed for the project, for use with an RDBMS software.

## Entities:
- User
    - UUID (primary)
    - Name
    - Username (unique)
    - E-Mail Address (unique)
    - Profile Image (optional)
    - Password
    - Mobile Number
    - Address
    - Transactions
- Product
    - Name
    - Type
    - Category (multi-valued)
    - Description
    - Features (multi-valued) (composite)
        - Key
        - Value

## Relationships:
(Note: Nested bullets denote relationship-specific attributes)
- _Product_ OFFERED BY _User_ **M:N**
    - Quantity
    - Price
- _User_ ADDS _Product_ PROVIDED BY _User_ TO CART **M:N:P**
    - Quantity
- _User_ PURCHASES _Item_ PROVIDED BY _User_ **M:N:P**
    - Order ID
    - Seller
    - Buyer
    - Product
    - Price
    - Payment Status
    - Date of Order
    - Date of Shipment

## Relations
- User
- Product
- CartItem
- Transaction