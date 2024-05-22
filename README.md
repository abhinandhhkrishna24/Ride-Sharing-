Ride Sharing API

Description:
The Ride Sharing API is a Django-based RESTful web service designed to facilitate ride sharing between drivers and riders. It allows users to register, request rides, view ride details, and update ride statuses. Additionally, it provides real-time ride tracking and ride matching functionalities.

Features:
1. User API:
   - Register: Allows users to create new accounts with unique usernames and passwords.
   - Login: Provides authentication for registered users to access protected endpoints.

2. Ride API:
   - Create Ride Request: Allows users to request a ride by providing pickup and dropoff locations.
   - View Ride Details: Enables users to view details of a specific ride, including its status, pickup and dropoff locations, and timestamps.
   - List Rides: Displays a list of all available rides.

3. Ride Status Updates:
   - Update Ride Status: Allows users to update the status of a ride, such as marking it as started, completed, or cancelled.

4. Ride Tracking 
   - Simulated Real-time Tracking: Implements a simulation of real-time ride tracking by periodically updating the ride's current location.

5. Ride Matching 
   - Ride Matching Algorithm: Implements an algorithm to match ride requests with available drivers based on proximity or other factors.
   - Accept Ride Request: Provides an API endpoint for drivers to accept ride requests, facilitating the ride matching process.

Endpoints:
- User Registration: POST /user/register/
- User Login: POST /user/login/
- Create Ride Request: POST /ride/create/
- View Ride Details: GET /ride/<int:pk>/
- List Rides: GET /ride/lists/
- Update Ride Status: PUT /ride/<int:pk>/update/
- Real-time Ride Tracking: Simulated real-time tracking implemented internally.
- Ride Matching: Matching algorithm applied internally; no specific endpoint.

