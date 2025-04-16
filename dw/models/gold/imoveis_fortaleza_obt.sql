WITH clean AS (
	SELECT 
		id
		, tipo
		, bairro
		, area
		, quartos
		, banheiros
		, vagas
		, condominio
		, preco
		, ROUND((preco/area)::DECIMAL, 2) AS preco_m2
	FROM {{ ref('silver_imoveis') }}
)
SELECT 
	*
	, CURRENT_TIMESTAMP AS ingestion_timestamp
FROM clean;