function validarDatos(){
    // Obtenemos los valores de los coeficientes
    var c1 = document.getElementById('coeficiente1').value;
    var c2 = document.getElementById('coeficiente2').value;
    var c3 = document.getElementById('coeficiente3').value;
    console.log(c1,c2,c3);
    document.getElementById('p1-output').value = "("+c1+") m^2 + ("+c2+") m + ("+c3+") = 0";
    var raices = document.getElementById('p2-output');
    // Calculamos el determinante
    var determinante = (c2*c2)-(4*c1*c3);
    if(determinante>0){
        // Tiene soluciones reales diferentes
        var m1 = (-c2+Math.sqrt(determinante))/(2*c1);
        var m2 = (-c2-Math.sqrt(determinante))/(2*c1);
        console.log("m1="+m1+" m2="+m2);
        var y1 = "e^("+m1+"x)";
        var y2 = "e^("+m2+"x)";
        console.log("y1="+y1+" y2="+y2);
        var sol_gral = "y = C1 "+y1+" + C2 "+y2;
        console.log(sol_gral);
    }else if(determinante==0){
        // Tiene soluciones iguales
        var m1 = (-c2+Math.sqrt(determinante))/(2*c1);
        var m2 = m1;
        console.log("m1="+m1+" m2="+m1);
        var y1 = "e^("+m1+"x)";
        var y2 = "xe^("+m1+"x)";
        console.log("y1="+y1+" y2="+y2);
        var sol_gral = "y = C1 "+y1+" + C2 "+y2;
        console.log(sol_gral);
    }else if(determinante<0){
        // Tiene soluciones imaginarias
        var theta = -c2/(2*c1);
        var beta = Math.sqrt(-determinante)/(2*c1);
        var m1 = theta+" + "+beta+"i";
        var m2 = theta+" - "+beta+"i";
        console.log("m1="+m1+" m2="+m2);
        var y1 = "e^("+theta+"x)cos("+beta+"x)";
        var y2 = "e^("+theta+"x)sen("+beta+"x)";
        console.log("y1="+y1+" y2="+y2);
        var sol_gral = "y = C1 "+y1+" + C2 "+y2;
        console.log(sol_gral);
    }
    document.getElementById('p2-output').value = "m1="+m1+"; m2="+m2;
    document.getElementById('p3-output').value = "y1="+y1+"; y2="+y2;
    document.getElementById('p4-output').value = sol_gral;
}