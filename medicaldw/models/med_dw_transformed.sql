-- dw_medical_transformed.sql

{{ config(materialized='table') }}

WITH filter_data AS (
    SELECT * 
    FROM {{ source('public', 'dw_medical') }}
)
SELECT 
   message_id,
   date,
   channel,
   text
FROM filter_data
