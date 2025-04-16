WITH clean AS(SELECT 
	MD5((ROW_NUMBER() OVER(PARTITION BY tipo))::VARCHAR) AS id
	, "_source" AS origem
	, tipo
	, CASE
		WHEN LOWER(bairro) LIKE '%praia do futuro%' THEN 'Praia do Futuro'
		ELSE bairro
	END AS bairro
	, area
	, quartos
	, banheiros
	, vagas
	, condominio
	, preco
FROM {{ ref('bronze_imoveis') }}
WHERE tipo IN ('Apartamento', 'Casa', 'Condomínio', 'Duplex', 'Triplex', 'Sobrado')
AND area >= 34
AND quartos > 0
AND banheiros > 0
AND preco >= 70000)

SELECT 
	*
	, CURRENT_TIMESTAMP AS ingestion_timestamp
FROM clean