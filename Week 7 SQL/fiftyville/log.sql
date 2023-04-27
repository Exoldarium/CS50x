-- Keep a log of any SQL queries you execute as you solve the mystery.

-- get all crime scene reports from Humphrey street on 28th of July
SELECT description
FROM crime_scene_reports
WHERE day = 28
AND month = 7
AND street = 'Humphrey Street';

-- get the origin city airport id
SELECT city, id
FROM airports
WHERE id IN
(
    SELECT origin_airport_id
    FROM flights
    WHERE day = 28
);

-- get the flight details but only flight originating in fiftyville
SELECT id, origin_airport_id, destination_airport_id, month, day, hour, minute
FROM flights
WHERE day = 28
AND origin_airport_id = 8;

-- get passport numbers from all the passenger flying out from fiftyville on 28 of July
SELECT passport_number
FROM passengers
WHERE flight_id IN (
    SELECT id
    FROM flights
    WHERE day = 28
    AND origin_airport_id = 8
);

-- get details of people who flew out of fiftyville on day of the incident and their cars are in bakery security logs
SELECT id, name, phone_number, license_plate
FROM people
WHERE passport_number IN (
    SELECT passport_number
    FROM passengers
    WHERE flight_id IN (
        SELECT id
        FROM flights
        WHERE day = 28
        AND origin_airport_id = 8
    )
AND license_plate IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE day = 28
    AND month = 7
    AND year = 2021
    )
);

-- check the bakery security logs on the day the incident happened and get the licencse plates
SELECT license_plate, activity, hour, minute
FROM bakery_security_logs
WHERE day = 28
AND month = 7
AND year = 2021
AND hour =10
AND minute > 15
AND activity = 'exit';

-- get the phone calls that happened at the day of the robbery and their license plates are in bakery logs and they flew out of the city on that day
SELECT duration, caller, receiver
FROM phone_calls
WHERE day = 28
AND month = 7
AND year = 2021
AND caller IN (
    SELECT phone_number
    FROM people
    WHERE passport_number IN (
    SELECT passport_number
    FROM passengers
    WHERE flight_id IN (
        SELECT id
        FROM flights
        WHERE day = 28
        AND origin_airport_id = 8
        )
    AND license_plate IN (
        SELECT license_plate
        FROM bakery_security_logs
        WHERE day = 28
        AND month = 7
        AND year = 2021
        AND hour > 10
        AND minute > 15
        AND activity = 'exit'
        )
    )
);


-- Kelsey plate = 0NTHK55, passport 8294398571, Diana plate = 322W7JE, passport = 3592750733, Bruce plate = 94KL13X passport = 5773159633, phone = (367) 555-5533

SELECT name
FROM people
WHERE license_plate IN (
   SELECT license_plate
    FROM bakery_security_logs
    WHERE day = 28
    AND month = 7
    AND year = 2021
    AND hour = 10
    AND minute BETWEEN 15 AND 25
    AND activity = 'exit'
);

-- get the name of people that were calling each other at the day of the robery and are in bakery logs
SELECT name, id
FROM people
WHERE phone_number IN ('(016) 555-9166', '(336) 555-0077', '(016) 555-9166', '(267) 555-2761', '(258) 555-5627', '(971) 555-6468');

-- check all interviews from 28th of July 2021
SELECT *
FROM interviews
WHERE day = 28
AND month = 7
AND year = 2021;

-- check transaction that at legget street as the thief was seen withdrawing money there
SELECT account_number
FROM atm_transactions
WHERE day = 28
AND month = 7
AND year = 2021
AND atm_location = 'Leggett Street';

-- check bank account numbers of people that were on the phone at the time of theft, that had cars at bakery parking lot and their call lasted less than a min
SELECT *
FROM bank_accounts
WHERE person_id IN (
    SELECT id
    FROM people
    WHERE phone_number IN ('(016) 555-9166', '(336) 555-0077', '(016) 555-9166', '(267) 555-2761', '(258) 555-5627')
);

-- check bank account of people who withdrew money on the day of robbery

SELECT name
FROM people
WHERE id IN (
    SELECT person_id
    FROM bank_accounts
    WHERE account_number IN (
        SELECT account_number
        FROM atm_transactions
        WHERE day = 28
        AND month = 7
        AND year = 2021
        AND atm_location = 'Leggett Street'
    )
);

-- check if Bruce was flying out
SELECT *
FROM flights
WHERE id IN (
    SELECT flight_id
    FROM passengers
    WHERE passport_number IN (5773159633)
);

-- Check phone calls that happened at the day of the robbery and were less than 1min
SELECT name, id
FROM people
WHERE phone_number IN (
    SELECT receiver
    FROM phone_calls
    WHERE day = 28
    AND month = 7
    AND year = 2021
    AND duration < 60
);

-- get people info that called at the day of the robbery and the calls were less than 1min
SELECT *
FROM people
WHERE id IN (
    SELECT  id
    FROM people
    WHERE phone_number IN (
        SELECT caller
        FROM phone_calls
        WHERE day = 28
        AND month = 7
        AND year = 2021
        AND duration < 60
    )
);

SELECT city
FROM airports
WHERE id = 4;



