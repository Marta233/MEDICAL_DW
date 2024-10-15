-- Materialize the model as a table for optimized querying
{{ config(materialized='table') }}

-- Select all data from the 'detections' table in the 'public' schema
SELECT * 
FROM public.detections;
