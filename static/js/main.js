function gonder() {
    var arr = [];
    var email = document.getElementById("email").value
    for(i=1;i<23;i++){
        if (document.getElementById(`${i}`).checked) {
            rate_value = document.getElementById(`${i}`).value;
            arr.push(rate_value);}
    }
        $.ajax({
        type: 'get',
        url: `/etkinlik_mail?email= ${email}&etkinlik=${arr.join(",")}`,
        success: function (data, textStatus, request) {
            console.log("dneme");
        },
        error: function (request, textStatus, errorThrown) {
            alert(1);
        }
    });

}


function temizle1(){
document.getElementById("1").checked = false;
document.getElementById("2").checked = false;
document.getElementById("3").checked = false;
document.getElementById("4").checked = false;
document.getElementById("5").checked = false;
}


function temizle2(){
document.getElementById("6").checked = false;
document.getElementById("7").checked = false;
document.getElementById("8").checked = false;
document.getElementById("9").checked = false;
document.getElementById("10").checked = false;
document.getElementById("11").checked = false;
}