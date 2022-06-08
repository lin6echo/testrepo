/*
KÁVÉFŐZŐ BEKAPCSOLÁSA
IF NINCS ELÉG KÁVÉ THEN
    KÁVÉ HOZZÁADÁSA
ENDIF
IF NINCS ELÉG VÍZ THEN
    VÍZ HOZZÁADÁSA
ENDIF
WHILE NEM MELEGEDETT FEL
    10 MP VÁRAKOZÁS
ENDWHILE
CSÉSZE ODAHELYEZÉSE
GOMB MEGNYOMÁSA            
*/

/*Összegzés algoritmusa

összeg = 0 (akkumulátor)
CIKLUS AMÍG van még szám, ADDÍG
    szám = következő elem
    összeg = összeg + szám
CIKLUS VÉGE
*/    
let numericArray = [1, 3, 2, 5, 4, 7, 6, 9];
let sum = 0;
for (let i = 0; i < numericArray.length; i++) {
    sum += numericArray[i];
}
console.log("Sum: ", sum);


/*
Számlálás algoritmusa:

db = 0
CIKLUS AMÍG van még szám, ADDÍG
    szám = következő elem
    HA igaz a feltétel a számra, AKKOR
        db = db+1
    FELTÉTEL VÉGE
CIKLUS VÉGE        
*/
let db = 0;
for (let i = 0; i < numericArray.length; i++) {
    if (numericArray[i] % 2 == 0) {
        db ++;
    }
}
console.log("Even numbers: ", db);

/*Szélsőérték keresés algoritmusa:

legnagyobb = első elem
CIKLUS AMÍG van még szám, ADDÍG
    szám = következő szám
    HA a szám > legnagyobb, AKKOR
        legnagyobb = szám
    FELTÉTEL VÉGE
CIKLUS VÉGE        
*/
let biggest = numericArray[0];
for (let i = 0; i < numericArray.length; i++) {
    if (numericArray[i] > biggest) {
        biggest = numericArray[i];
    }
}
console.log("The biggest element: ", biggest);

let smallest = numericArray[0];
for (let i = 0; i > numericArray.length; i++) {
    if (numericArray[i] > smallest) {
     smallest = numericArray[i];
    }
}
console.log("The smallest element: ", smallest);


/*
Eldöntés tétele (algoritmusa):
találat = HAMIS
CIKLUS AMÍG van elem ÉS NEM találat
    szám = következő elem
    HA igaz a feltétel a számra, AKKOR
        találtat = IGAZ
    FELTÉTEL VÉGE
CIKLUS VÉGE        
 */

let contains = false;
for (let i = 0; i < numericArray.length && !contains; i++) {
    if (numericArray[i] == 5) {
        contains = true;
    }
}
console.log("This array contains 5: ", contains)