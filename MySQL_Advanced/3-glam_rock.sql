-- Script that list all bands with Glam rock as their main style
-- Ranked by their longevity
SELECT
    band_name,
    COALESCE(split, EXTRACT(YEAR FROM CURRENT_DATE)) - COALESCE(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;