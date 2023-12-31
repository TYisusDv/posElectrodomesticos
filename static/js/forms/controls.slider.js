class SliderControls {
  constructor() {
    "undefined" != typeof noUiSlider
      ? (this._initHorizontalBasic(),
        this._initSliderDisabled(),
        this._initSliderVerticalBasic(),
        this._initSliderTooltip(),
        this._initSliderTooltipVertical(),
        this._initSliderSteps(),
        this._initSliderRound(),
        this._initPips(),
        this._initPipsVertical(),
        this._initTopLabel(),
        this._initFilled(),
        this._initFloatingLabel())
      : console.log("noUiSlider is undefined!");
  }
  _initHorizontalBasic() {
    document.getElementById("sliderHorizontalBasic") &&
      noUiSlider.create(document.getElementById("sliderHorizontalBasic"), {
        start: [20],
        connect: [!0, !1],
        range: { min: 0, max: 100 },
      });
  }
  _initSliderDisabled() {
    document.getElementById("sliderDisabled") &&
      noUiSlider.create(document.getElementById("sliderDisabled"), {
        start: [20],
        connect: [!0, !1],
        range: { min: 0, max: 100 },
      });
  }
  _initSliderVerticalBasic() {
    document.getElementById("sliderVerticalBasic") &&
      noUiSlider.create(document.getElementById("sliderVerticalBasic"), {
        start: [20],
        orientation: "vertical",
        connect: [!0, !1],
        direction: "rtl",
        range: { min: 0, max: 100 },
      });
  }
  _initSliderTooltip() {
    document.getElementById("sliderTooltip") &&
      noUiSlider.create(document.getElementById("sliderTooltip"), {
        start: [20, 80],
        connect: !0,
        tooltips: [!0, !0],
        range: { min: 0, max: 100 },
      });
  }
  _initSliderTooltipVertical() {
    document.getElementById("sliderTooltipVertical") &&
      noUiSlider.create(document.getElementById("sliderTooltipVertical"), {
        start: [20, 80],
        connect: !0,
        orientation: "vertical",
        tooltips: [!0, !0],
        direction: "rtl",
        range: { min: 0, max: 100 },
      });
  }
  _initSliderSteps() {
    document.getElementById("sliderStep") &&
      noUiSlider.create(document.getElementById("sliderStep"), {
        start: [4e3],
        step: 1e3,
        tooltips: !0,
        connect: [!0, !1],
        range: { min: [1e3], max: [1e4] },
      });
  }
  _initSliderRound() {
    document.getElementById("sliderRound") &&
      noUiSlider.create(document.getElementById("sliderRound"), {
        start: [4e3],
        step: 1e3,
        tooltips: !0,
        connect: [!0, !1],
        range: { min: [1e3], max: [1e4] },
        format: {
          to: function (e) {
            return Math.round(e);
          },
          from: function (e) {
            return Number(e);
          },
        },
      });
  }
  _initPips() {
    document.getElementById("sliderPips") &&
      noUiSlider.create(document.getElementById("sliderPips"), {
        start: [10, 90],
        step: 10,
        tooltips: !0,
        connect: !0,
        range: { min: 0, max: 100 },
        pips: {
          mode: "steps",
          density: 5,
          format: {
            to: function (e) {
              return "$ " + e;
            },
            from: function (e) {
              return Number(e.replace("$", ""));
            },
          },
        },
        format: {
          to: function (e) {
            return "$ " + e;
          },
          from: function (e) {
            return Number(e.replace("$", ""));
          },
        },
      });
  }
  _initPipsVertical() {
    document.getElementById("sliderPips") &&
      noUiSlider.create(document.getElementById("sliderPipsVertical"), {
        start: [10, 90],
        step: 10,
        tooltips: !0,
        connect: !0,
        orientation: "vertical",
        range: { min: 0, max: 100 },
        pips: {
          mode: "steps",
          density: 5,
          format: {
            to: function (e) {
              return "$ " + e;
            },
            from: function (e) {
              return Number(e.replace("$", ""));
            },
          },
        },
        format: {
          to: function (e) {
            return "$ " + e;
          },
          from: function (e) {
            return Number(e.replace("$", ""));
          },
        },
      });
  }
  _initTopLabel() {
    document.getElementById("sliderHorizontalTopLabel") &&
      noUiSlider.create(document.getElementById("sliderHorizontalTopLabel"), {
        start: [20],
        connect: [!0, !1],
        range: { min: 0, max: 100 },
      });
  }
  _initFilled() {
    document.getElementById("sliderHorizontalFilled") &&
      noUiSlider.create(document.getElementById("sliderHorizontalFilled"), {
        start: [20],
        connect: [!0, !1],
        range: { min: 0, max: 100 },
      });
  }
  _initFloatingLabel() {
    document.getElementById("sliderHorizontalFloatingLabel") &&
      noUiSlider.create(
        document.getElementById("sliderHorizontalFloatingLabel"),
        { start: [20], connect: [!0, !1], range: { min: 0, max: 100 } }
      );
  }
}
