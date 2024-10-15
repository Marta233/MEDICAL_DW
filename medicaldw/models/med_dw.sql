-- Materialize the model as a table for optimized querying
{{ config(materialized='table') }}

-- Select all columns from the 'dw_medical' table in the 'public' schema
SELECT * 
FROM public.dw_medical;
