with staging as (
    select * from {{ ref("stg_garmin_activities") }}
),

final as (
    SELECT 
        file_source as id_treino,
        CAST(ingested_at as DATE) as data_ingestao,
        
        sum(distancia_km) as distancia_total_km,
        sum(tempo_total_segundos) as tempo_total_segundos,
        round(avg(fc_media), 0) as fc_media,
        max(fc_maxima) as fc_pico,
        sum(calorias) as calorias_totais,

        case 
            when sum(distancia_km) > 0
            then (sum(tempo_total_segundos) / sum(distancia_km))
            else 0
        end as pace_medio_treino_segundos_km

    FROM staging
    GROUP BY 1, 2 
)

SELECT * FROM final