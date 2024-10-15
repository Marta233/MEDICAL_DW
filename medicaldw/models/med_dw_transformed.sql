-- Materialize the model as a table for optimized querying
{{ config(materialized='table') }}

-- Create a CTE to filter data from the 'dw_medical' source table
WITH filter_data AS (
    SELECT * 
    FROM {{ source('public', 'dw_medical') }}
)

-- Select specific columns from the filtered data
SELECT 
   message_id,   -- Unique message ID
   date,         -- Date of the message
   channel,      -- Channel name where the message was written
   text          -- Extracted message text
FROM filter_data;
