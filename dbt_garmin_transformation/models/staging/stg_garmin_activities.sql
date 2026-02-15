with source as (
    SELECT * FROM  {{ source("garmin_raw", "garmin_activities") }}
),

renamed as (
    SELECT 
        file_source,
        ingested_at,

        tipo_de_etapa,
        volta,
        intervalo,

        distancia::float as distancia_km,
        calorias::int as calorias,
        fc_media::int as fc_media,
        fc_maxima::int as fc_maxima,
        cadencia_de_corrida_media::int as cadencia_media,

        
        (CAST(CAST(split_part(tempo, ':', 1) AS FLOAT) AS INT) * 60) + CAST(CAST(split_part(tempo, ':', 2) AS FLOAT) AS INT) as tempo_total_segundos,
        
        (CAST(CAST(split_part(ritmo_medio, ':', 1) AS FLOAT) AS INT) * 60) + CAST(CAST(split_part(ritmo_medio, ':', 2) AS FLOAT) AS INT) as ritmo_medio_segundos
    FROM source
)

SELECT * FROM renamed