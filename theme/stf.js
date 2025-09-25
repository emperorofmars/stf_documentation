
/* Sphinx fixes */

for(let e of document.querySelectorAll(".sidebar-tree .caption")) {
	e.setAttribute("aria-level", "2");
}

document.querySelector(".sidebar-tree li.current-page").setAttribute("aria-selected", "true");

/* Furo theme fixes */

document.querySelector(".content-icon-container").setAttribute("role", "complementary");
document.querySelector(".content-icon-container .view-this-page .muted-link").setAttribute("title", "View this page's source"); /* The default "View this page" doesn't quite make sense imho. */


/* STF temp fixes, turn TBD buttons into a AAA error */

let e;
if(e = document.querySelector(".sd-btn-outline-secondary.ignore")) e.setAttribute("role", "presentation");

