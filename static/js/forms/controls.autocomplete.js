class AutocompleteControls {
  constructor() {
    "undefined" != typeof AutocompleteCustom
      ? (this._initStrictArray(),
        this._initLooseArray(),
        this._initArrayOfObjects(),
        this._initJson(),
        this._initTopLabel(),
        this._initFilled(),
        this._initFloatingLabel())
      : console.log("AutocompleteCustom is undefined!");
  }
  _initStrictArray() {
    null !== document.getElementById("strictArray") &&
      new AutocompleteCustom("strictArray", "strictArrayResults", {
        data: {
          src: [
            "Anpan",
            "Basler Brot",
            "Cheesymite Scroll",
            "Dorayaki",
            "Fougasse",
            "Guernsey Gâche",
            "Kalach",
            "Lefse",
            "Matzo",
            "Naan",
            "Paratha",
            "Pistolet",
            "Rewena",
            "Shirmal",
            "Teacake",
            "Vienna Bread",
            "Zopf",
          ],
        },
        placeHolder: "Search",
        searchEngine: "strict",
        highlight: !0,
      });
  }
  _initLooseArray() {
    null !== document.getElementById("looseArray") &&
      new AutocompleteCustom("looseArray", "looseArrayResults", {
        data: {
          src: [
            "Anpan",
            "Basler Brot",
            "Cheesymite Scroll",
            "Dorayaki",
            "Fougasse",
            "Guernsey Gâche",
            "Kalach",
            "Lefse",
            "Matzo",
            "Naan",
            "Paratha",
            "Pistolet",
            "Rewena",
            "Shirmal",
            "Teacake",
            "Vienna Bread",
            "Zopf",
          ],
        },
        placeHolder: "Search",
        searchEngine: "loose",
        highlight: !0,
      });
  }
  _initArrayOfObjects() {
    null !== document.getElementById("arrayOfObjects") &&
      new AutocompleteCustom("arrayOfObjects", "arrayOfObjectsResults", {
        data: {
          src: [
            { id: 1, name: "Anpan" },
            { id: 2, name: "Basler Brot" },
            { id: 3, name: "Cheesymite Scroll" },
            { id: 4, name: "Dorayaki" },
            { id: 5, name: "Fougasse" },
            { id: 6, name: "Guernsey Gâche" },
            { id: 7, name: "Kalach" },
            { id: 8, name: "Lefse" },
            { id: 9, name: "Matzo" },
            { id: 10, name: "Naan" },
            { id: 11, name: "Paratha" },
            { id: 12, name: "Pistolet" },
            { id: 13, name: "Rewena" },
            { id: 14, name: "Shirmal" },
            { id: 15, name: "Teacake" },
            { id: 16, name: "Vienna Bread" },
            { id: 17, name: "Anpan" },
            { id: 18, name: "Zopf" },
          ],
          key: ["name"],
        },
        placeHolder: "Search",
        searchEngine: "strict",
        onSelection: (e) => {
          (document.getElementById("arrayOfObjects").value =
            e.selection.value.name),
            document.getElementById("arrayOfObjects").blur();
        },
      });
  }
  _initJson() {
    null !== document.getElementById("jsonData") &&
      new AutocompleteCustom("jsonData", "jsonDataResults", {
        data: {
          src: async () => {
            const e = await fetch("json/search.json");
            return await e.json();
          },
          key: ["label"],
          cache: !1,
        },
        placeHolder: "Search",
        searchEngine: "loose",
        onSelection: (e) => {
          (document.getElementById("jsonData").value = e.selection.value.label),
            document.getElementById("jsonData").blur();
        },
      });
  }
  _initFloatingLabel() {
    null !== document.getElementById("floatingLabelInput") &&
      new AutocompleteCustom(
        "floatingLabelInput",
        "floatingLabelInputResults",
        {
          data: {
            src: [
              "Anpan",
              "Basler Brot",
              "Cheesymite Scroll",
              "Dorayaki",
              "Fougasse",
              "Guernsey Gâche",
              "Kalach",
              "Lefse",
              "Matzo",
              "Naan",
              "Paratha",
              "Pistolet",
              "Rewena",
              "Shirmal",
              "Teacake",
              "Vienna Bread",
              "Zopf",
            ],
          },
          placeHolder: "Search",
          searchEngine: "strict",
          highlight: !0,
        }
      );
  }
  _initTopLabel() {
    null !== document.getElementById("topLabelInput") &&
      new AutocompleteCustom("topLabelInput", "topLabelInputResults", {
        data: {
          src: [
            "Anpan",
            "Basler Brot",
            "Cheesymite Scroll",
            "Dorayaki",
            "Fougasse",
            "Guernsey Gâche",
            "Kalach",
            "Lefse",
            "Matzo",
            "Naan",
            "Paratha",
            "Pistolet",
            "Rewena",
            "Shirmal",
            "Teacake",
            "Vienna Bread",
            "Zopf",
          ],
        },
        placeHolder: "",
        searchEngine: "strict",
        highlight: !0,
      });
  }
  _initFilled() {
    null !== document.getElementById("filledInput") &&
      new AutocompleteCustom("filledInput", "filledInputResults", {
        data: {
          src: [
            "Anpan",
            "Basler Brot",
            "Cheesymite Scroll",
            "Dorayaki",
            "Fougasse",
            "Guernsey Gâche",
            "Kalach",
            "Lefse",
            "Matzo",
            "Naan",
            "Paratha",
            "Pistolet",
            "Rewena",
            "Shirmal",
            "Teacake",
            "Vienna Bread",
            "Zopf",
          ],
        },
        placeHolder: "Search",
        searchEngine: "strict",
        highlight: !0,
      });
  }
}
