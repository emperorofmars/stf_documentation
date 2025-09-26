
/* Sphinx fixes */

for(let e of document.querySelectorAll(".sidebar-tree .caption"))
	e.setAttribute("aria-level", "2");

document.querySelector(".sidebar-tree li.current-page").setAttribute("aria-selected", "true");

/* Furo theme fixes */

document.querySelector(".content-icon-container").setAttribute("role", "complementary");
document.querySelector(".content-icon-container .view-this-page .muted-link").setAttribute("title", "View this page's source"); /* The default "View this page" doesn't quite make sense imho. */

for(let e of document.querySelectorAll(".toc-tree ul"))
	if(e.getHTML().trimStart() === "")
		e.remove();

/* STF temp fixes, turn TBD buttons into a AAA error */

for(let e of document.querySelectorAll(".sd-btn-outline-secondary.ignore"))
	e.setAttribute("role", "presentation");

