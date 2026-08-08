(function () {
  "use strict";

  /* ---- read lang pref ---- */
  var lang = localStorage.getItem("langPref") || "id";

  /* ---- get post id from URL ?id=xxx ---- */
  var params = new URLSearchParams(window.location.search);
  var postId = params.get("id");

  /* ---- find post ---- */
  var postIndex = -1;
  var post = null;
  for (var i = 0; i < POSTS.length; i++) {
    if (POSTS[i].id === postId) {
      postIndex = i;
      post = POSTS[i];
      break;
    }
  }

  /* ---- if not found, redirect home ---- */
  if (!post) {
    window.location.href = "Landing.html";
    return;
  }

  /* ---- render article ---- */
  function render(l) {
    var content = document.getElementById("postContent");
    var title = l === "en" ? post.title_en : post.title_id;
    var date = l === "en" ? post.date_en : post.date_id;
    var tag = l === "en" ? post.tag_en : post.tag_id;
    var body = l === "en" ? post.content_en : post.content_id;
    var image = post.image || "";
    var imageAlt = post.image_alt || title;

    document.title = "Nixon — " + title;

    var imageMarkup = image
      ? '<figure class="post-cover-wrap">' +
        '<img src="' +
        image +
        '" alt="' +
        imageAlt +
        '" class="post-cover-image" />' +
        "</figure>"
      : "";

    var glossaryMarkup =
      '<section class="post-glossary">' +
      '<h2 class="glossary-title">' +
      (l === "en" ? "Glossary" : "Glosarium") +
      "</h2>" +
      '<ul class="glossary-list">';

    GLOSSARY.forEach(function (item) {
      var term = l === "en" ? item.term_en : item.term_id;
      var desc = l === "en" ? item.definition_en : item.definition_id;

      glossaryMarkup +=
        "<li>" + "<strong>" + term + ":</strong> " + desc + "</li>";
    });

    glossaryMarkup += "</ul></section>";

    content.innerHTML =
      '<article class="post-article">' +
      imageMarkup +
      '<div class="post-meta">' +
      '<span class="mono post-tag">' +
      tag +
      "</span>" +
      '<span class="mono post-date">' +
      date +
      "</span>" +
      "</div>" +
      '<h1 class="post-title display">' +
      title +
      "</h1>" +
      '<hr class="post-divider" />' +
      '<div class="post-body">' +
      body +
      "</div>" +
      glossaryMarkup +
      "</article>";

    /* translate static UI */
    document.querySelectorAll("[data-id][data-en]").forEach(function (el) {
      el.innerHTML =
        l === "en" ? el.getAttribute("data-en") : el.getAttribute("data-id");
    });
    document.documentElement.lang = l;
    var btn = document.getElementById("langToggle");
    if (btn) btn.textContent = l === "en" ? "ID" : "EN";
  }
  render(lang);

  /* ---- prev / next ---- */
  var prevPost = POSTS[postIndex - 1] || null;
  var nextPost = POSTS[postIndex + 1] || null;

  var prevEl = document.getElementById("prevPost");
  var nextEl = document.getElementById("nextPost");
  var prevTitle = document.getElementById("prevTitle");
  var nextTitle = document.getElementById("nextTitle");

  if (prevPost) {
    prevEl.href = "post.html?id=" + prevPost.id;
    prevTitle.textContent =
      lang === "en" ? prevPost.title_en : prevPost.title_id;
  } else {
    prevEl.style.visibility = "hidden";
  }
  if (nextPost) {
    nextEl.href = "post.html?id=" + nextPost.id;
    nextTitle.textContent =
      lang === "en" ? nextPost.title_en : nextPost.title_id;
  } else {
    nextEl.style.visibility = "hidden";
  }

  /* ---- reading progress bar ---- */
  var bar = document.getElementById("readProgress");
  window.addEventListener(
    "scroll",
    function () {
      var scrollTop = window.scrollY;
      var docH = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.width = (docH > 0 ? (scrollTop / docH) * 100 : 0) + "%";
    },
    { passive: true },
  );

  /* ---- lang toggle ---- */
  var langBtn = document.getElementById("langToggle");
  if (langBtn) {
    langBtn.addEventListener("click", function () {
      lang = lang === "id" ? "en" : "id";
      localStorage.setItem("langPref", lang);

      /* fade */
      var nodes = document.querySelectorAll(
        "[data-id][data-en], .post-body, .post-title, .post-tag, .post-date",
      );
      nodes.forEach(function (n) {
        n.classList.add("fade-out");
      });
      setTimeout(function () {
        render(lang);
        /* update nav titles */
        if (prevTitle && prevPost)
          prevTitle.textContent =
            lang === "en" ? prevPost.title_en : prevPost.title_id;
        if (nextTitle && nextPost)
          nextTitle.textContent =
            lang === "en" ? nextPost.title_en : nextPost.title_id;
        document.querySelectorAll("[data-id][data-en]").forEach(function (n) {
          n.classList.remove("fade-out");
        });
      }, 280);
    });
  }

  /* ---- music toggle ---- */
  (function () {
    var musicBtn = document.getElementById("musicToggle");
    var audio = document.getElementById("bgm");
    if (!musicBtn || !audio) return;
    var playing = false;
    musicBtn.addEventListener("click", function () {
      if (playing) {
        audio.pause();
        musicBtn.classList.remove("is-active");
      } else {
        audio.play().catch(function () {});
        musicBtn.classList.add("is-active");
      }
      playing = !playing;
    });
  })();
})();
