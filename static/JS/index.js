/* 
┌──────────────────────────┐
│ ί JS Dictionary          │
└──────────────────────────┘
	[1] = LIBRARY:
        [1.1] = Color Palette
		->  [2.1.1] = Light Theme
		->  [2.1.1] = Dark Theme
        [1.2] = Shadows
	[2] = Functions:
        [2.1] = Theme Changer
        ->  [2.1.1] = Transition
        ->  [2.1.2] = Button
*/  
var r = document.querySelector(':root');

/* 
┌──────────────────────────┐
│ [1.1] Color Palette      │
└──────────────────────────┘ */
/* [1.1.1] ─── Dark Theme ───*/
function dark_set() {
	// Primary Color
	r.style.setProperty('--Primary', 'rgb(208, 188, 255)');
	r.style.setProperty('--On-Primary', 'rgb(56, 30, 114)');
	r.style.setProperty('--Primary-Container', 'rgb(79, 55, 139)');
	r.style.setProperty('--On-Primary-Container', 'rgb(234, 221, 255)');
	// Secondary Color
	r.style.setProperty('--Secondary', 'rgb(204, 194, 220)');
	r.style.setProperty('--On-Secondary', 'rgb(51, 45, 65)');
	r.style.setProperty('--Secondary-Container', 'rgb(74, 68, 88)');
	r.style.setProperty('--On-Secondary-Container', 'rgb(232, 222, 248)');
	// Tertiary Color
	r.style.setProperty('--Tertiary', 'rgb(239, 184, 200)');
	r.style.setProperty('--On-Tertiary', 'rgb(73, 37, 50)');
	r.style.setProperty('--Tertiary-Container', 'rgb(99, 59, 72)');
	r.style.setProperty('--On-Tertiary-Container', 'rgb(255, 216, 228)');
	// Error Color
	r.style.setProperty('--Error', 'rgb(242, 184, 181)');
	r.style.setProperty('--On-Error', 'rgb(96, 20, 16)');
	// Background
	r.style.setProperty('--Background', 'rgb(28, 27, 31)'); // L10
	r.style.setProperty('--On-Background', 'rgb(230, 225, 229)');
	// Surface
	r.style.setProperty('--Surface', 'rgb(49, 48, 51)'); // L20
	r.style.setProperty('--Surface-L25', 'rgb(61, 59, 62)');
	r.style.setProperty('--Surface-L30', 'rgb(72, 70, 73)');
	r.style.setProperty('--Surface-L35', 'rgb(84, 82, 85)');
	r.style.setProperty('--On-Surface', 'rgb(230, 225, 229)');
	r.style.setProperty('--On-Surface-Large-TXT', 'rgba(230, 225, 229, 0.87)');
	r.style.setProperty('--On-Surface-Medium-TXT', 'rgba(230, 225, 229, 0.6)');
	r.style.setProperty('--On-Surface-Small-TXT', 'rgba(230, 225, 229, 0.38)');
	// Others
	r.style.setProperty('--TXT-Weight', 'lighter');
	r.style.setProperty('--On-Color-TXT-Weight', 'bold');
	r.style.setProperty('--TXT-Selection', 'rgba(255, 255, 255, 0.2)');
	r.style.setProperty('--Active-Item', '110%');
}

/* [1.1.2] ── Light Theme ───*/
function light_set() {
	// Primary Color
	r.style.setProperty('--Primary', 'rgb(102, 80, 164)');
	r.style.setProperty('--On-Primary', 'rgb(255, 255, 255)');
	r.style.setProperty('--Primary-Container', 'rgb(234, 221, 255)');
	r.style.setProperty('--On-Primary-Container', 'rgb(33, 0, 93)');
	// Secondary Color
	r.style.setProperty('--Secondary', 'rgb(125, 82, 96)');
	r.style.setProperty('--On-Secondary', 'rgb(255, 255, 255)');
	r.style.setProperty('--Secondary-Container', 'rgb(232, 222, 248)');
	r.style.setProperty('--On-Secondary-Container', 'rgb(29, 25, 43)');
	// Tertiary Color
	r.style.setProperty('--Tertiary', 'rgb(125, 82, 96)');
	r.style.setProperty('--On-Tertiary', 'rgb(255, 255, 255)');
	r.style.setProperty('--Tertiary-Container', 'rgb(255, 216, 228)');
	r.style.setProperty('--On-Tertiary-Container', 'rgb(49, 17, 29)');
	// Error Color
	r.style.setProperty('--Error', 'rgb(179, 37, 30)');
	r.style.setProperty('--On-Error', 'rgb(255, 255, 255)');
	// Background
	r.style.setProperty('--Background', 'rgb(255, 251, 254)');  // L10
	r.style.setProperty('--On-Background', 'rgb(28, 27, 31)');
	// Surface
	r.style.setProperty('--Surface', 'rgb(234, 230, 243)');  // L20
	r.style.setProperty('--Surface-L25', 'rgb(222, 219, 232)');
	r.style.setProperty('--Surface-L30', 'rgb(211, 208, 221)');
	r.style.setProperty('--Surface-L35', 'rgb(199, 196, 209)');
	r.style.setProperty('--On-Surface', 'rgb(28, 27, 31)');
	r.style.setProperty('--On-Surface-Large-TXT', 'rgba(28, 27, 31, 0.87)');
	r.style.setProperty('--On-Surface-Medium-TXT', 'rgba(28, 27, 31, 0.6)');
	r.style.setProperty('--On-Surface-Small-TXT', 'rgba(28, 27, 31, 0.38)');
	// Others
	r.style.setProperty('--TXT-Weight', 'normal');
	r.style.setProperty('--On-Color-TXT-Weight', 'normal');
	r.style.setProperty('--TXT-Selection', 'rgba(0, 0, 0, 0.2)');
	r.style.setProperty('--Active-Item', '90%');
}

/* 
┌──────────────────────────┐
│ [1.2] Shadows			   │
└──────────────────────────┘ */
function shadows() {
	// Umbra, Penumbra, Ambient
	// x, y, blur, spread, color
	r.style.setProperty('--Shadow-1DP', '0 0 2px 0 rgba(0,0,0,0.14), 0 2px 2px 0 rgba(0,0,0,0.12), 0 1px 3px 0 rgba(0,0,0,0.2)');
	r.style.setProperty('--Shadow-2DP', '0 0 4px 0 rgba(0,0,0,0.14), 0 3px 4px 0 rgba(0,0,0,0.12), 0 1px 5px 0 rgba(0,0,0,0.2)');
	r.style.setProperty('--Shadow-3DP', '0 3px 3px 0 rgba(0,0,0,0.14), 0 3px 4px 0 rgba(0,0,0,0.12), 0 1px 8px 0 rgba(0,0,0,0.2)');
	r.style.setProperty('--Shadow-4DP', '0 2px 4px 0 rgba(0,0,0,0.14), 0 4px 5px 0 rgba(0,0,0,0.12), 0 1px 10px 0 rgba(0,0,0,0.2)');
	r.style.setProperty('--Shadow-8DP', '0 8px 10px 1px rgba(0,0,0,0.14), 0 3px 14px 3px rgba(0,0,0,0.12), 0 4px 15px 0 rgba(0,0,0,0.2)');
	r.style.setProperty('--Shadow-9DP', '0 9px 12px 1px rgba(0,0,0,0.14), 0 3px 16px 2px rgba(0,0,0,0.12), 0 5px 6px 0 rgba(0,0,0,0.2)');
	r.style.setProperty('--Shadow-12DP', '0 12px 17px 2px rgba(0,0,0,0.14), 0 5px 22px 4px rgba(0,0,0,0.12), 0 7px 8px 0 rgba(0,0,0,0.2)');
	r.style.setProperty('--Shadow-16DP', '0 16px 24px 2px rgba(0,0,0,0.14), 0 6px 30px 5px rgba(0,0,0,0.12), 0 8px 10px 0 rgba(0,0,0,0.2)');
	r.style.setProperty('--Shadow-24DP', '0 24px 38px 3px rgba(0,0,0,0.14), 0 9px 46px 8px rgba(0,0,0,0.12), 0 11px 15px 0 rgba(0,0,0,0.2)');
	r.style.setProperty('--Shadow-6DP', '0 6px 10px 0 rgba(0,0,0,0.14), 0 1px 18px 0 rgba(0,0,0,0.12), 0 3px 5px 0 rgba(0,0,0,0.2)');
}
shadows()

/* 
┌──────────────────────────┐
│ [2.1] Theme Changer	   │
└──────────────────────────┘ */
/* [2.1.1] ── Transition ───*/
const transition = (obj, trTime) =>{// La función crea la transición y luego la elimina para evitar problemas.
	let trRemove = trTime * 1000 + 100;
	obj.style.setProperty("transition", `${trTime}s`);
	setTimeout(()=>{
	  obj.style.removeProperty("transition");
	},trRemove);
};

/* [2.1.2] ──── Button ─────*/
const theme = document.querySelector(".theme"); 
const body = document.getElementsByTagName("body");// Seleccionamos el cuerpo del documento.
const all = body[0].getElementsByTagName("*");// Selecciona todo lo que está dentro del documento.
let light = false;
dark_set(); // El Dark Mode es el predefinido
theme.addEventListener("click", () => {
	if (light == false) {
		light_set();
		light = true;
	} else {
	  dark_set();
	  light = false;
	}
	theme.classList.toggle("down"); // Cuando se agrega la clase "down" el icono gira 180 deg.
	transition(body[0],0.2);
	for (let i = 0; i < all.length; i++) {// Este bucle es el encargado de añadir la transición de tema a todos los elementos dentro cuerpo (body).
	  transition(all[i], 0.2);
	}
});