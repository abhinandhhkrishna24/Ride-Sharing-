# Ride Sharing API

This API provides endpoints for user registration, login, ride management, and real-time ride tracking.

## Endpoints

### User Management

- `POST /user/register/`: Register a new user.
- `POST /user/login/`: Login with username and password.

### Ride Management

- `POST /ride/create/`: Create a new ride request.
- `GET /ride/<ride_id>/`: Retrieve details of a specific ride by its ID.
- `GET /ride/lists/`: List all rides.
- `PUT /ride/<ride_id>/update/`: Update the status of a ride.
- `GET /ride/available/`: Find and match available rides with drivers.
- `PUT /ride/accept/<ride_id>/`: Accept a ride request by the driver.

## Authentication

- User registration and login endpoints require no authentication.
- All other endpoints require authentication via JWT token. Include the token in the Authorization header as follows: `Authorization: Bearer <token>`.

## Pagination

- Ride lists endpoint (`/ride/lists/`) supports pagination with a default page size of 10 rides per page.
