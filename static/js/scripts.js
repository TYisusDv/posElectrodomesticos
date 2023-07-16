class Scripts {
  constructor() {
    this._initSettings(),
      this._initVariables(),
      this._addListeners(),
      this._init();
  }
  _init() {
    setTimeout(() => {
      document.documentElement.setAttribute("data-show", "true"),
        document.body.classList.remove("spinner"),
        this._initBase(),
        this._initCommon(),
        this._initPages();
    }, 100);
  }
  _initBase() {
    if ("undefined" != typeof Nav) {
      new Nav(document.getElementById("nav"));
    }
    if ("undefined" != typeof Search) {
      new Search();
    }
    "undefined" != typeof AcornIcons && new AcornIcons().replace();
  }
  _initCommon() {
    if ("undefined" != typeof Common) {
      new Common();
    }
  }
  _initPages() {
    if ("undefined" != typeof AccountSettings) {
      new AccountSettings();
    }
    if ("undefined" != typeof Analysis) {
      new Analysis();
    }
    if ("undefined" != typeof Communitylist) {
      new Communitylist();
    }
    if ("undefined" != typeof ServicesDatabase) {
      new ServicesDatabase();
    }
    if ("undefined" != typeof ServicesDatabaseAdd) {
      new ServicesDatabaseAdd();
    }
    if ("undefined" != typeof ServicesDatabaseDetail) {
      new ServicesDatabaseDetail();
    }
    if ("undefined" != typeof ServicesStorage) {
      new ServicesStorage();
    }
    if ("undefined" != typeof SupportDocs) {
      new SupportDocs();
    }
    if ("undefined" != typeof SupportTicketsDetail) {
      new SupportTicketsDetail();
    }
  }
  _initSettings() {
    if ("undefined" != typeof Settings) {
      new Settings({
        attributes: {
          placement: "horizontal",
          layout: "fluid",
          color: "light-sky",
          navcolor: "default",
        },
        showSettings: !0,
        storagePrefix: "acorn-service-provider-",
      });
    }
  }
  _initVariables() {
    if ("undefined" != typeof Variables) {
      new Variables();
    }
  }
  _addListeners() {
    document.documentElement.addEventListener(
      Globals.menuPlacementChange,
      (e) => {
        setTimeout(() => {
          window.dispatchEvent(new Event("resize"));
        }, 25);
      }
    ),
      document.documentElement.addEventListener(Globals.layoutChange, (e) => {
        setTimeout(() => {
          window.dispatchEvent(new Event("resize"));
        }, 25);
      }),
      document.documentElement.addEventListener(
        Globals.menuBehaviourChange,
        (e) => {
          setTimeout(() => {
            window.dispatchEvent(new Event("resize"));
          }, 25);
        }
      );
  }
}
window.addEventListener("DOMContentLoaded", () => {
  void 0 !== Scripts && new Scripts();
}),
  "undefined" != typeof Dropzone && (Dropzone.autoDiscover = !1);
