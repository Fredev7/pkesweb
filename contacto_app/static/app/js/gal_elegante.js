const $portfolio = document.querySelector("sec-portfolio-js");
const $modalImgPortfolio = document.querySelector(".img-modal-js");

$portfolio.addEventListener("click", (e) => {
    
    if(e.target.classList.contains("img-btn-modal-js")) {
        //SRC 
       let urlImg = e.target.atributes[0].nodeValue;
       //ADD MODEL
       $modalImgPortfolio.src = urlImg; 
    }
});