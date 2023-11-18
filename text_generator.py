# Скрипт генерує текст для index.html на основі таблиці csv
# текст необхідно потім скопіювати в index.html - після тегу "textBlocks"


import pandas as pd
import os


text = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta content="width=device-width, initial-scale=1" name="viewport" />

    <!-- OpenGraph Meta Tags -->
    <meta property="fb:app_id" content="329250623807149" />
    <meta property="og:site_name" content="ТЕКСТИ.ORG.UA" />
    <meta property="og:type" content="website" />
    <meta
      property="og:title"
      content="На шляху до моря"
    />
    <meta
      property="og:image"
      content="https://texty.org.ua/d/2023/way_to_sea/pic/cover.jpg"
    />
    <meta
      property="og:description"
      content="Кілометри окопів, безкраї мінні поля, сотні бліндажів, підземні тунелі й цілі “земляні фортеці”. Які оборонні споруди доводиться “прогризати” ЗСУ на півдні України"
    />
    <meta
      property="og:url"
      content="https://texty.org.ua/d/2023/way_to_sea/"
    />

    <!-- Twitter Card Meta Tags -->
    <meta name="twitter:site" content="@textyorgua" />
    <meta property="twitter:account_id" content="49572937" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta
      name="twitter:url"
      content="https://texty.org.ua/d/2023/way_to_sea/"
    />
    <meta
      name="twitter:title"
      content="The Path to the Sea "
    />
    <meta
      name="twitter:description"
     content="Кілометри окопів, безкраї мінні поля, сотні бліндажів, підземні тунелі й цілі “земляні фортеці”. Які оборонні споруди доводиться “прогризати” ЗСУ на півдні України" 
     />
    <meta name="twitter:image:width" content="1200" />
    <meta name="twitter:image:height" content="630" />

    <!-- Other Meta Tags -->
    <meta
      name="title"
      content="The Path to the Sea "
    />
    <meta
      name="description"
      content="Кілометри окопів, безкраї мінні поля, сотні бліндажів, підземні тунелі й цілі “земляні фортеці”. Які оборонні споруди доводиться “прогризати” ЗСУ на півдні України"
    />

    <script
      src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"
      type="text/javascript"
    ></script>

    <link rel="stylesheet" href="css/styles.css" />
    <script src="https://unpkg.com/scrollama"></script>

    <script
      src="https://kit.fontawesome.com/043a4ca43b.js"
      crossorigin="anonymous"
    ></script>

    <!-- UIkit CSS -->
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/uikit@3.14.3/dist/css/uikit.min.css"
    />

    <!-- UIkit JS -->
    <script src="https://cdn.jsdelivr.net/npm/uikit@3.14.3/dist/js/uikit.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/uikit@3.14.3/dist/js/uikit-icons.min.js"></script>

    <link
      href="https://api.tiles.mapbox.com/mapbox-gl-js/v1.13.0/mapbox-gl.css"
      rel="stylesheet"
    />
    <script src="https://api.tiles.mapbox.com/mapbox-gl-js/v1.13.0/mapbox-gl.js"></script>

    <title>
      The Path to the Sea 
    </title>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-EXHPRQFFLB"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());

        gtag('config', 'G-EXHPRQFFLB');
    </script>

    <!-- Meta Pixel Code -->
    <script>
        !function (f, b, e, v, n, t, s) {
            if (f.fbq) return; n = f.fbq = function () {
                n.callMethod ?
                    n.callMethod.apply(n, arguments) : n.queue.push(arguments)
            };
            if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0';
            n.queue = []; t = b.createElement(e); t.async = !0;
            t.src = v; s = b.getElementsByTagName(e)[0];
            s.parentNode.insertBefore(t, s)
        }(window, document, 'script',
            'https://connect.facebook.net/en_US/fbevents.js');
        fbq('init', '528421947990222');
        fbq('track', 'PageView');
    </script>
    <noscript><img height="1" width="1" style="display:none"
            src="https://www.facebook.com/tr?id=528421947990222&ev=PageView&noscript=1" /></noscript>
    <!-- End Meta Pixel Code -->


<link rel="preload" as="image" href="./pic/01.png" />
<link rel="preload" as="image" href="./pic/02.png" />
<link rel="preload" as="image" href="./pic/03.png" />
<link rel="preload" as="image" href="./pic/04.png" />
<link rel="preload" as="image" href="./pic/13.png" />
<link rel="preload" as="image" href="./pic/6.png" />
<link rel="preload" as="image" href="./pic/7.png" />
<link rel="preload" as="image" href="./pic/8.png" />
<link rel="preload" as="image" href="./pic/arrow_1.png" />

<link
      rel="preload"
      href="./data/front_line.geojson"
      as="fetch"
      crossorigin="anonymous"
    />

    <link
      rel="preload"
      href="./data/labels.geojson"
      as="fetch"
      crossorigin="anonymous"
    />

    <link
      rel="preload"
      href="./data/lines_merged.geojson"
      as="fetch"
      crossorigin="anonymous"
    />
    <link
      rel="preload"
      href="./data/points_merged.geojson"
      as="fetch"
      crossorigin="anonymous"
    />

    <link
      rel="preload"
      href="./data/poly_merged.geojson"
      as="fetch"
      crossorigin="anonymous"
    />


<link
    rel="preload"
    href="./fonts/proxima-nova-black.woff"
    as="font"
    crossorigin
  />

     <link
    rel="preload"
    href="./fonts/proxima-nova-bold.woff"
    as="font"
    crossorigin
  />

       <link
    rel="preload"
    href="./fonts/proxima-nova-medium.woff"
    as="font"
    crossorigin
  />

         <link
    rel="preload"
    href="./fonts/proxima-nova-regular.woff"
    as="font"
    crossorigin
  />

           <link
    rel="preload"
    href="./fonts/proxima-nova-semibold.woff"
    as="font"
    crossorigin
  />
  </head>

  <body>

  <header>
    <a class="texty-logo" href="/">
      <img
        class="desktop-only"
        src="https://texty.org.ua/static/core/images/white_logo.svg"
        alt="Тексти.org.ua"
      />
      <img
        class="mobile-only"
        src="https://texty.org.ua/static/core/images/white_logo.svg"
        alt="Тексти.org.ua"
      />
    </a>

    <nav class="rubrics-container">
      <div class="rubric r1">
        <a
          href="https://texty.org.ua/tag/khid-vijny/"
          class="special-devil-animation"
          ><span>Хід Війни</span></a
        >
      </div>
      <div class="rubric r2">
        <a href="https://texty.org.ua/tag/dezinformatsija/"
          ><span>#Інфовійна</span></a
        >
      </div>
      <div class="rubric r2">
        <a href="https://texty.org.ua/tag/eng/"><span>#English</span></a>
      </div>
      <div class="rubric r5">
        <a href="https://texty.org.ua/articles/"><span>Статті</span></a>
      </div>
      <div class="rubric r6">
        <a href="https://texty.org.ua/fragments/"><span>Фрагменти</span></a>
      </div>
      <div class="rubric r7">
        <a href="https://texty.org.ua/selected/"><span>Вибір редакції</span></a>
      </div>

      <div class="rubric r-burger">
        <input id="menu__toggle" type="checkbox" />
        <label class="menu__btn" for="menu__toggle">
          <span>
          </span>
        </label>

        <div class="menu__box">
          <ul class="items__container">
            <li class="mobile-only">
              <a class="menu__item" href="https://texty.org.ua/tag/khid-vijny/"
                >Хід Війни</a
              >
            </li>
            <li class="mobile-only">
              <a
                class="menu__item"
                href="https://texty.org.ua/tag/dezinformatsija/"
                >#Інфовійна</a
              >
            </li>
            <li class="mobile-only">
              <a class="menu__item" href="https://texty.org.ua/tag/eng/"
                >#English</a
              >
            </li>

            <li>
              <a class="menu__item" href="https://texty.org.ua/projects/"
                >Журналістика даних</a
              >
            </li>
            <li>
              <a class="menu__item" href="https://texty.org.ua/articles/"
                >Статті</a
              >
            </li>
            <li>
              <a class="menu__item" href="https://texty.org.ua/fragments/"
                >Фрагменти</a
              >
            </li>
            <li>
              <a class="menu__item" href="https://texty.org.ua/selected/"
                >Вибір редакції</a
              >
            </li>
            <li>
              <a class="menu__item" href="https://texty.org.ua/donate/#/"
                >Наш Дата-Арт</a
              >
            </li>
            <li>
              <a
                class="menu__item"
                href="https://texty.org.ua/texty.org.ua/d/principles/"
                >Принципи</a
              >
            </li>
            <li>
              <a class="menu__item" href="https://texty.org.ua/tag/hrafik-dnja/"
                >Графік дня</a
              >
            </li>
          </ul>
        </div>
      </div>
      <div id="search" class="rubric"></div>
    </nav>
  </header>



    <div style="height: 100vh; margin-bottom: 5%">
      <img id="cover" src="https://texty.org.ua/d/2023/way_to_sea/pic/cover.jpg" />
      <div class="header-wrapper">
        <div id="socio-icons">
          <!--fb-->
          <a
            href="https://www.facebook.com/sharer/sharer.php?u=https://texty.org.ua/d/2023/way_to_sea/"
            target="_blank"
            class="share-btn"
          >
            <div class="icon-wrapper">
              <img id="fb" src="pic/facebook.png" />
            </div>
          </a>
          <!--tw -->
          <a
            href="https://twitter.com/intent/tweet?text=https://texty.org.ua/d/2023/way_to_sea/"
            target="_blank"
            class="share-btn"
          >
            <div class="icon-wrapper">
              <img id="tw" src="pic/twitter.png" />
            </div>
          </a>
        </div>
      </div>
      <div id="title-wrapper">
        <h1>НА ШЛЯХУ ДО МОРЯ</h1>
        <h2>Кілометри окопів, безкраї мінні поля, сотні бліндажів, підземні тунелі й цілі “земляні фортеці”. Які оборонні споруди доводиться “прогризати” ЗСУ на півдні України
</h2>
      </div>
    </div>
    <div id="autors">
      <p>Автор: 
      <a
        href="https://texty.org.ua/author/denys-hubashov/"
        target="_blank"
        > Денис Губашов</a
      >
      </p><p>Дизайн: 
      <a
        href="https://texty.org.ua/author/nadja-kelm/"
        target="_blank"
        > Надя Кельм</a
      ></p>
    </div>
      <div class='blackP'>
        <p id="leadone">
          ТЕКСТи реконструювати російську оборону лінію на півдні. Ми дослідили на супутникових знімках  за червень-вересень 2023 
          року оборонні споруди окупантів ще не взятого міста Токмак і сіл Роботине (яке нещовдавно звільнили) й Вербове.</p>
       

        <p id="planet"> Супутникові знімки для проекту надані компанією <a href="https://www.planet.com/">Planet Labs</a>  </p>
        <p>Після звільнення Роботиного розпочалася велика битва за Токмак, яка теоретично може стати фінальним актом активної воєнної кампанії 2023 року. </p>
        <p>
        Токмак — ключ до Мелітополя, і битва за це чимале місто може тривати кілька місяців з перемінним успіхом, але стане ключовою для “розрубування” сухопутного коридору з окупованого Криму до окупованих східних областей.
        </p>
        <p>Класична радянська лінія оборони із масивними полями та широкою лінією забезпечення - мінними полями, виносними позицями, спостережними пунктами. </p>
        <p>
        Оборона росіян, яку вони побудували з осені минулого року, — це сотні кілометрів безперервних траншей, бліндажів, ДОТів, ДЗОТів, окремих опорних пунктів — за розміром як середньовічний форт, який може кілька діб оборонятись автономно, а також налагоджена логістика, система малих складів боєкомплекту, тилові бази радіорозвідки, загонів БПЛА, артилеристів. </p>
      </div>
      <div class="adaptive-image"></div>
      <div class='blackP'>
        <p>Окупанти зараз стягнули під Токмак значні резерви новостворену загальновійськову 25 армію та 76 та 7 десантні дивізії. Зараз якраз вони намагаються атакувати фланги наступаючих сил ЗСУ. </p>
        <p>Ми намагалися хоча б частково показати, як побудовано російські укріплення на півдні. Оборонні лінії потужні, тому, схоже, їх штурм може затягнутися на місяці.</p>
      </div>
      
      <div id="espreso-wrapper">  <p>Інформаційні партнери: </p><img id="espreso-logo" src="pic/espreso_logo.png" /> <img id="logo-24" src="pic/24_logo.png" /> </div>
      <div class='blackP'>
      <p><span style = "color: #BA2828;">Червона </span> зона на карті - окуповані території </p>
      </div>
      <section style="margin-top: 10vh; margin-bottom: 10vh;">
        <div id="mapBlocks">
          <div id="map"></div>
        </div>
        <div id="textBlocks">"""


def save_html_to_file(html_content, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_content)


df = pd.read_csv(
    """https://docs.google.com/spreadsheets/d/e/2PACX-1vTKpe1iyz6X9akGptwjrrPQS0YQb7W3WkO1fq9YgbLu33IIo8C-LHdaRRQpAwaVhEa1SAcI-AxnmI6u/pub?gid=0&single=true&output=csv"""
)
print(df.head())

for index, row in df.iterrows():
    # print(row['text'])
    # print(row['step'])
    # print(row['coords'])
    # print(row['zoom'])
    text += f"""<div class="step" datazoom="{row['zoom']}" zoom_mobile="{row['zoom_mobile']}" coords_mobile="{row['coords_mobile']}" datacoords ="{str(row['coords'])}" datapoly="{row['datapoly']}" datapoints="{row['datapoints']}" datalines="{row['datalines']}" datalabels="{row['labels']}">"""
    text += f"""<h5>{row['step']}</h5>"""
    text += f"""<p>{row['text']}</p>"""
    if pd.notna(row["images"]):
        text += f"""<p class="img-header">{row['img_header']}<p>"""
        text += f"""<div><img src='pic/{row['images']}' loading="lazy" style="display: block; margin: auto;  max-height: 90vh;"></div>"""

    if pd.notna(row["video"]):
        text += f"""<div class="video-container">"""
        text += f"""<video class='video' src="./pic/{row['video']}" autoplay loop muted>>
                <source src="./pic/{row["video"]}" type="video/mp4">
                Your browser does not support the video tag.
                </video></div>"""
    text += f"""</div>"""

text += """</div>

        <div id="scroll-final"></div>
      </section>
      <div>
       <div class='blackP'>
          <p>
            Від супутникової розвідки сховатися майже неможливо — маючи абсолютно невибагливий компʼютер та доступ до інтернету, ви самостійно можете отримати безкоштовні 
            супутникові знімки та знайти, де ховається ворог. 
          </p>
          <p>
            Український контрнаступ — одна із найскладніших та кровопролитніших військових операцій у східній Европі з часів Другої світової війни. 
            Підтримуйте сили оборони та допомагайте - на фронті зараз важко.
          </p>
        </div>
      </div>
    <script src="js/mymap.js "></script>
  <div class="share-article">
    <div class="share-title">Поширити:</div>

    <div class="sb fb">
      <a
        class="share-btn"
        href="https://www.facebook.com/sharer/sharer.php?u=https://texty.org.ua/d/2023/way_to_sea/"
        target="_blank"
      >
        <img
          src="./pic/facebook-logo-white.png"
          alt="Тексти.org.ua - Facebook"
      /></a>
    </div>

    <div class="sb tw">
      <a
        class="share-btn"
        href="https://twitter.com/intent/tweet?text=https://texty.org.ua/d/2023/way_to_sea/"
        target="_blank"
      >
        <img
          src="./pic/twitter-logo-white.png"
          alt="Тексти.org.ua - Twitter"
      /></a>
    </div>

    <div class="sb tl">
      <a
        class="share-btn"
        href="https://telegram.me/share/url?url=https://texty.org.ua/d/2023/way_to_sea/"
        target="_blank"
      >
        <img
          src="./pic/telegram-logo-white.png"
          alt="Тексти.org.ua - Telegram"
      /></a>
    </div>

    <div class="sb hr">
      <a
        href="https://texty.org.ua/support/"
        target="_blank"
        title="Пожертвувати"
        ><img
          src="https://texty.org.ua/static/core/images/hrn2.svg"
          alt="Знак гривні"
      /></a>
    </div>
  </div>

  <h3 id="read-more-title">Читайте також:</h3>
  <div id="custom-read-more">
    <a
      id="rm-1"
      class="rm"
      href="https://texty.org.ua/articles/101984/vkopani-u-kamin-yak-vlashtovani-ukrayinski-okopy-na-shidnomu-fronti/"
      target="_blank"
    >
      <h2>
        Шрами війни. Як влаштовані українські окопи на східному фронті (Інфографіка)
      </h2>
    </a>
    <a id="rm-2" class="rm" href="https://texty.org.ua/projects/110472/masove-vbyvstvo-na-zhytomyrskij-trasi-mapa-hronolohiya-ta-rozsliduvannya-rosijskoho-zlochynu/" target="_blank">
      <h2>Масове вбивство на Житомирській трасі: мапа, хронологія та розслідування російського злочину</h2>
    </a>
    <a
      id="rm-3"
      class="rm"
      href="https://texty.org.ua/d/2023/mariupol_chronicles/"
      target="_blank"
    >
      <h2>
Війна. Початок.
Маріуполь</h2>
    </a>
  </div>

  <form
    class="subscribe subscribe-footer"
    action="//texty.us2.list-manage.com/subscribe/post?u=6a4d05e311e165b44ca8ccb21&amp;id=cc81c0bd84"
    method="post"
    id="mc-embedded-subscribe-form"
    name="mc-embedded-subscribe-form"
    target="_blank"
    novalidate=""
  >
    <div class="subscribe-call">
      <p>Отримуйте найкращі статті на e-mail (раз на два тижні)</p>
    </div>

    <div class="mail-input-container">
      <i class="icon-envelope"></i>
      <input
        placeholder="E-mail"
        type="email"
        value=""
        name="EMAIL"
        required=""
      />

      <div style="position: absolute; left: -5000px" aria-hidden="true">
        <input
          type="text"
          name="b_6a4d05e311e165b44ca8ccb21_cc81c0bd84"
          tabindex="-1"
          value=""
        />
      </div>
    </div>

    <button
      type="submit"
      value="Додайте мене у список!"
      name="subscribe"
      class="subscribe-button"
    >
      Підписатися
    </button>

    <div class="last-release">
      <p>
        <a
          target="_blank"
          href="https://mailchi.mp/c92cacc5dab9/texty_newsletter_0412"
          >Подивитись свіжий випуск</a
        >
      </p>
    </div>
  </form>
    <footer>
    <div id="logo-copyright">
      <a class="texty-logo" href="/">
        <img
          class="desktop-only"
          src="https://texty.org.ua/static/core/images/white_logo.svg"
          alt="Тексти.org.ua"
        />
        <img
          class="mobile-only"
          style="max-width: 150px"
          src="https://texty.org.ua/static/core/images/white_logo.svg"
          alt="Тексти.org.ua"
        />
      </a>
      <div class="copyright">
        <p><span class="copyleft">©</span> 2010—2022 Texty.org.ua</p>
      </div>
    </div>

    <div id="guide-block">
      <ul class="links1">
        <li>
          <a href="https://texty.org.ua/p/about/">Про нас</a>
          <a href="https://texty.org.ua/p/about-en/">(About us)</a>
        </li>

        <li>
          <a href="https://texty.org.ua/articles/">Статті</a>
          <a href="https://texty.org.ua/articles/feed.xml">(RSS)</a>
        </li>

        <li>
          <a href="https://texty.org.ua/fragments/">Фрагменти</a>
          <a href="https://texty.org.ua/fragments/feed.xml">(RSS)</a>
        </li>

        <li>
          <a href="https://texty.org.ua/p/mailing-lists/">Розсилки Текстів</a>
        </li>
        <li><a href="https://texty.org.ua/selected/">Вибір редакції</a></li>
        <li><a href="https://texty.org.ua/tag/eng/">#English</a></li>
      </ul>

      <ul class="links2">
        <li><a href="https://texty.org.ua/projects/">Журналістика даних</a></li>
        <li><a href="https://texty.org.ua/d/socio/">Фальшиві соціологи</a></li>
        <li><a href="https://fgz.texty.org/">Фейкогриз</a></li>
        <li>
          <a href="https://texty.org.ua/tag/dezinformatsija/">Дезінформація</a>
        </li>
        <li>
          <a href="https://texty.org.ua/tag/disinfomonitor/">Disinfomonitor</a>
        </li>
      </ul>

      <ul class="links3">
        <li>
          <a href="https://texty.org.ua/support/" target="_blank"
            >Підтримай нас!</a
          >
        </li>
        <li>
          <a href="https://texty.org.ua/donate/#/" target="_blank"
            >Наш дата-арт</a
          >
        </li>
        <li><a href="https://texty.org.ua/tag/hrafik-dnja/">Графік Дня</a></li>
        <li><a href="https://texty.org.ua/archive-blogs/">Архів блогів</a></li>
        <li><a href="https://texty.org.ua/archive-books/">Архів книг</a></li>
      </ul>
    </div>

    <div id="social_buttons">
      <aside class="follow-us floating-right-autoplace">
        <p class="piece-title">Стежити:</p>
        <div class="follow-us-tiles">
          <a href="https://www.facebook.com/TEXTY.org.ua/" target="_blank">
            <img
              src="https://texty.org.ua/static/core/images/facebook.png"
              alt="Тексти.org.ua - Facebook"
            />
          </a>
          <a href="https://www.instagram.com/texty.org.ua/" target="_blank">
            <img
              src="https://texty.org.ua/static/core/images/instagram.png"
              alt="Тексти.org.ua - Instagram"
            />
          </a>

          <a href="https://telegram.me/textyorgua" target="_blank">
            <img
              src="https://texty.org.ua/static/core/images/telegram.png"
              alt="Тексти.org.ua - Telegram"
            />
          </a>

          <a href="https://twitter.com/textyorgua" target="_blank">
            <img
              src="https://texty.org.ua/static/core/images/twitter.png"
              alt="Тексти.org.ua - Twitter"
            />
            <div class="bottom-caption">UA</div>
          </a>

          <a href="https://twitter.com/textyorgua_eng" target="_blank">
            <img
              src="https://texty.org.ua/static/core/images/twitter.png"
              alt="Texty.org.ua - Twitter in English"
            />
            <div class="bottom-caption">EN</div>
          </a>

          <a
            href="https://invite.viber.com/?g2=AQB%2FXntNTr9qKU788eLrk2Pf0b6l6nENMg%2BfjGAND9XZpEdGLM88SHbJcZBVh2Q5"
            target="_blank"
          >
            <img
              src="https://texty.org.ua/static/core/images/viber.png"
              alt="Тексти.org.ua - Viber"
            />
          </a>
        </div>
      </aside>
    </div>

    <div id="license">
      <p>
        Матеріали ТЕКСТИ.org.ua можна використовувати згідно ліцензії
        <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank"
          >Creative Commons із зазначенням авторства, CC BY</a
        >
        (переклад ліцензії
        <a
          href="https://creativecommons.org/licenses/by/4.0/legalcode.uk"
          target="_blank"
          >українською</a
        >). Велике прохання ставити гіперпосилання в першому чи другому абзаці
        вашого матеріалу.
      </p>
      <p></p>
    </div>
  </footer>
    

    <script type="text/javascript">
      var _gaq = _gaq || [];
      _gaq.push(["_setAccount", "UA-18136548-1"]);
      _gaq.push(["_trackPageview"]);
      (function () {
        var ga = document.createElement("script");
        ga.type = "text/javascript";
        ga.async = true;
        ga.src =
          ("https:" == document.location.protocol ? "https://" : "http://") +
          "stats.g.doubleclick.net/dc.js";
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(ga, s);
      })();
    </script>
    <script src="https://texty.org.ua/static/TopProjectsBannerD.js"></script>
    <div id="crosshair">
     <!-- <div class="vertical"></div>
    <div class="horizontal"></div> -->
</div>

  </body>
</html>"""


save_html_to_file(text, "rus_tranches_2_web/index.html")


#  приклад виводу
#  <div class="step">
#             <h5>6</h5>
#             <p>
#               Супутникові знімки також дають можливість моніторити позиції
#               росіян, ближчі до лінії фронту, визначати їх опорні позиції,
#               артилерійські позиції, бази й навіть окремі окопи. <br /><br />
#               Ми проаналізували доступні супутникові знімки в період 1-10 липня
#               2022 року та спробували визначити, як влаштовані позиції росіян
#               між Миколаєвом і Херсоном.
#             </p>
# <p>Також можна визначити, що це саме українська контрбатарейна боротьба, якщо визначити напрямок, із якого здійснювали обстріл.
#                       <img src='pic/111.jpg' style="width: 100%; margin-top: 3vh;"></p>
#           </div>
