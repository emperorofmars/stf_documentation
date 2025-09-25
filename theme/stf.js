
/* Sphinx fixes */

for(let e of document.querySelectorAll(".sidebar-tree .caption")) {
	//e.removeAttribute("role");
	e.setAttribute("role", "presentation");
}


/* Furo theme fixes */

document.querySelector(".content-icon-container").setAttribute("role", "complementary");
document.querySelector(".content-icon-container .view-this-page .muted-link").setAttribute("title", "View this page's source"); /* The default "View this page" doesn't quite make sense imho. */


/* STF temp fixes, turn TBD buttons into a AAA error */

document.querySelector(".sd-btn-outline-secondary.ignore").setAttribute("role", "presentation");

