<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FRØN - Patrocinadores</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial,sans-serif;
}

body{
    background:
    radial-gradient(circle at top,#111 0%,#050505 70%);
    color:white;
    min-height:100vh;
    overflow-x:hidden;
    padding:20px;
}

body::before{
    content:"";
    position:fixed;
    width:100%;
    height:100%;
    top:0;
    left:0;
    background:
    repeating-linear-gradient(
        90deg,
        rgba(0,255,136,0.03),
        rgba(0,255,136,0.03) 1px,
        transparent 1px,
        transparent 40px
    );
    pointer-events:none;
}

.container{
    max-width:1300px;
    margin:auto;
}

.header{
    text-align:center;
    padding:30px 20px;
    margin-bottom:40px;
}

.header h1{
    font-size:4em;
    color:#00ff88;
    letter-spacing:5px;
    text-shadow:
    0 0 10px #00ff88,
    0 0 20px #00ff88,
    0 0 40px #00ff88;
    margin-bottom:10px;
}

.header p{
    color:#bdbdbd;
    font-size:1.2em;
}

.top-benefits{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:20px;
    margin-bottom:40px;
}

.benefit-card{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(0,255,136,0.3);
    border-radius:18px;
    padding:20px;
    text-align:center;
    backdrop-filter:blur(8px);
    box-shadow:0 0 15px rgba(0,255,136,0.1);
    transition:0.3s;
}

.benefit-card:hover{
    transform:translateY(-5px);
    box-shadow:0 0 25px rgba(0,255,136,0.3);
}

.benefit-card h2{
    color:#00ff88;
    margin-bottom:10px;
    font-size:1.3em;
}

.benefit-card p{
    color:#d4d4d4;
    line-height:1.5;
}

.sponsors-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
    gap:30px;
}

.sponsor-card{
    background:rgba(255,255,255,0.06);
    border-radius:20px;
    padding:25px;
    text-align:center;
    backdrop-filter:blur(12px);
    border:1px solid rgba(255,255,255,0.1);
    transition:0.3s;
    position:relative;
    overflow:hidden;
}

.sponsor-card::before{
    content:"";
    position:absolute;
    top:0;
    left:-100%;
    width:100%;
    height:100%;
    background:linear-gradient(
        90deg,
        transparent,
        rgba(0,255,136,0.08),
        transparent
    );
    transition:0.7s;
}

.sponsor-card:hover::before{
    left:100%;
}

.sponsor-card:hover{
    transform:translateY(-8px);
    box-shadow:0 0 30px rgba(0,255,136,0.2);
}

.sponsor-image{
    width:150px;
    height:150px;
    margin:0 auto 20px;
    border-radius:15px;
    overflow:hidden;
    display:flex;
    align-items:center;
    justify-content:center;
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.08);
}

.sponsor-image img{
    width:100%;
    height:100%;
    object-fit:contain;
}

.sponsor-card h3{
    color:#00ff88;
    margin-bottom:10px;
    font-size:1.5em;
}

.sponsor-card p{
    color:#d0d0d0;
    line-height:1.6;
    margin-bottom:8px;
}

.special-offer{
    margin-top:15px;
    padding:15px;
    border-radius:12px;
    background:rgba(0,255,136,0.08);
    border:1px solid rgba(0,255,136,0.4);
}

.special-offer p{
    color:#00ff88;
    font-weight:bold;
}

.start-button-container{
    text-align:center;
    margin:50px 0 30px;
}

.start-button{
    display:inline-block;
    padding:18px 55px;
    border-radius:60px;
    text-decoration:none;
    font-size:1.3em;
    font-weight:bold;
    color:#000;
    background:linear-gradient(45deg,#00ff88,#00ffaa);
    box-shadow:
    0 0 20px rgba(0,255,136,0.5),
    0 0 40px rgba(0,255,136,0.3);
    transition:0.3s;
}

.start-button:hover{
    transform:scale(1.05);
    box-shadow:
    0 0 30px rgba(0,255,136,0.8),
    0 0 60px rgba(0,255,136,0.5);
}

.footer{
    text-align:center;
    margin-top:50px;
    padding:25px;
    color:#666;
    border-top:1px solid rgba(255,255,255,0.08);
}

.status-online{
    margin-top:10px;
    color:#00ff88;
    font-weight:bold;
    animation:pulse 1.5s infinite;
}

@keyframes pulse{
    0%{
        opacity:1;
    }
    50%{
        opacity:0.4;
    }
    100%{
        opacity:1;
    }
}

@media(max-width:768px){

    .header h1{
        font-size:2.5em;
    }

    .sponsors-grid{
        grid-template-columns:1fr;
    }

    .top-benefits{
        grid-template-columns:1fr;
    }

}
</style>
</head>

<body>

<div class="container">

    <div class="header">
        <h1>FRØN</h1>
        <p>Patrocinadores Oficiais • Sistema Premium</p>
        <div class="status-online">
            ● ONLINE
        </div>
    </div>

    <!-- BENEFÍCIOS -->
    <div class="top-benefits">

        <div class="benefit-card">
            <h2>📶 4G GRÁTIS</h2>
            <p>
                Continue conectado com acesso liberado e estabilidade.
            </p>
        </div>

        <div class="benefit-card">
            <h2>▶ YouTube Prime</h2>
            <p>
                Benefícios premium ativos para melhor experiência.
            </p>
        </div>

        <div class="benefit-card">
            <h2>🌍 Tradução de Réels</h2>
            <p>
                Tradução automática para vídeos e conteúdos do Instagram.
            </p>
        </div>

    </div>

    <!-- SPONSORS -->
    <div class="sponsors-grid">

        <!-- Corre de Seda -->
        <div class="sponsor-card">
            <div class="sponsor-image">
                <img src="corre.png" alt="Corre de Seda">
            </div>

            <h3>CORRE DE SEDA</h3>

            <p>Produtos de tabacaria de qualidade</p>
            <p>TóxicSkull√ a subir código</p>
        </div>

        <!-- Automotive -->
        <div class="sponsor-card">
            <div class="sponsor-image">
                <img src="lg.png" alt="Automotive Estética">
            </div>

            <h3>AUTOMOTIVE ESTÉTICA</h3>

            <p>Serviço especializado em lanternagem</p>
            <p>Mão de obra profissional</p>
        </div>

        <!-- Volvaco -->
        <div class="sponsor-card">
            <div class="sponsor-image">
                <img src="volvaco.png" alt="Volvaco">
            </div>

            <h3>VOLVACO</h3>

            <p>Mecânica especializada Volvo</p>
            <p>Carreta cavalinho FH/FM Volvo diesel</p>
            <p>Mão de obra qualificada</p>
        </div>

        <!-- Quintal -->
        <div class="sponsor-card">
            <div class="sponsor-image">
                <img src="logo.png" alt="Quintal do Peixe">
            </div>

            <h3>QUINTAL DO PEIXE</h3>

            <p>Experiência gastronômica única</p>

            <div class="special-offer">
                <p>🎯 Ajuda sem pré com almoço por conta da casa</p>
            </div>
        </div>

        <!-- Paraíso -->
        <div class="sponsor-card">
            <div class="sponsor-image">
                <img src="paraíso.png" alt="Paraíso das Bebidas">
            </div>

            <h3>DISTRIBUIDORA PARAÍSO DAS BEBIDAS</h3>

            <p>Melhores bebidas da região</p>

            <div class="special-offer">
                <p>📍 Ipatinga - MG</p>
                <p>🎁 Sempre não cobra nada para TóxicSkull</p>
            </div>
        </div>

    </div>

    <!-- BOTÃO -->
    <div class="start-button-container">
        <a href="https://furiadanoiteplay.com.br"
           target="_blank"
           class="start-button">
            INICIAR
        </a>
    </div>

    <!-- FOOTER -->
    <div class="footer">
        <p>© 2026 FRØN • Todos os direitos reservados</p>
    </div>

</div>

</body>
</html>