class Analysis {
  constructor() {
    (this._streamingLineChart = null),
      (this._streamingBarChart = null),
      (this._progressBars = []),
      "undefined" != typeof Chart && "undefined" != typeof ChartsExtend
        ? (this._initStreamingLineChart(), this._initStreamingBarChart())
        : console.error("[CS] Chart or ChartsExtend is undefined."),
      "undefined" != typeof ProgressBar
        ? this._initProgressCircle()
        : console.error("[CS] ProgressBar is undefined."),
      this._initEvents();
  }
  _onRefresh(t) {
    t.config.data.datasets.forEach(function (t) {
      t.data.push({ x: moment(), y: Math.round(50 * Math.random()) + 25 });
    });
  }
  _initStreamingLineChart() {
    if (document.getElementById("streamingLineChart")) {
      const t = document.getElementById("streamingLineChart").getContext("2d");
      this._streamingLineChart = new Chart(t, {
        type: "line",
        options: {
          plugins: {
            crosshair: ChartsExtend.Crosshair(),
            datalabels: { display: !1 },
            streaming: { frameRate: 30 },
          },
          responsive: !0,
          maintainAspectRatio: !1,
          scales: {
            yAxes: [
              {
                gridLines: {
                  display: !0,
                  lineWidth: 1,
                  color: Globals.separator,
                  drawBorder: !1,
                },
                ticks: {
                  beginAtZero: !0,
                  padding: 20,
                  fontColor: Globals.alternate,
                  min: 0,
                  max: 100,
                  stepSize: 25,
                },
              },
            ],
            xAxes: [
              {
                gridLines: { display: !1 },
                ticks: { display: !1 },
                type: "realtime",
                realtime: {
                  duration: 2e4,
                  refresh: 1e3,
                  delay: 3e3,
                  onRefresh: this._onRefresh,
                },
              },
            ],
          },
          legend: { display: !1 },
          tooltips: ChartsExtend.ChartTooltipForCrosshair(),
        },
        data: {
          labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
          datasets: [
            {
              label: "",
              borderColor: Globals.primary,
              pointBackgroundColor: Globals.primary,
              pointBorderColor: Globals.primary,
              pointHoverBackgroundColor: Globals.primary,
              pointHoverBorderColor: Globals.primary,
              borderWidth: 2,
              pointRadius: 2,
              pointBorderWidth: 2,
              pointHoverRadius: 3,
              fill: !1,
            },
          ],
        },
      });
    }
  }
  _initStreamingBarChart() {
    if (document.getElementById("streamingBarChart")) {
      const t = document.getElementById("streamingBarChart").getContext("2d");
      this._streamingBarChart = new Chart(t, {
        type: "bar",
        data: {
          labels: [],
          datasets: [
            {
              label: "Breads",
              data: [],
              borderColor: Globals.primary,
              backgroundColor: "rgba(" + Globals.primaryrgb + ",0.1)",
              borderWidth: 2,
            },
          ],
        },
        options: {
          cornerRadius: parseInt(Globals.borderRadiusMd),
          plugins: {
            crosshair: ChartsExtend.Crosshair(),
            datalabels: { display: !1 },
            streaming: { frameRate: 30 },
          },
          responsive: !0,
          maintainAspectRatio: !1,
          title: { display: !1 },
          scales: {
            xAxes: [
              {
                ticks: { display: !1 },
                type: "realtime",
                realtime: {
                  duration: 2e4,
                  refresh: 1e3,
                  delay: 3e3,
                  onRefresh: this._onRefresh,
                },
                gridLines: { display: !1 },
              },
            ],
            yAxes: [
              {
                gridLines: {
                  display: !0,
                  lineWidth: 1,
                  color: Globals.separator,
                  drawBorder: !1,
                },
                ticks: {
                  beginAtZero: !0,
                  stepSize: 25,
                  min: 0,
                  max: 100,
                  padding: 20,
                },
              },
            ],
          },
          tooltips: ChartsExtend.ChartTooltip(),
          legend: { display: !1 },
        },
      });
    }
  }
  _progressCircleDestroy() {
    for (let t = 0; t < this._progressBars.length; t++)
      this._progressBars[t].destroy();
    this._progressBars = [];
  }
  _progressCircleUpdate() {
    this._progressCircleDestroy(), this._initProgressCircle();
  }
  _initProgressCircle() {
    document.querySelectorAll(".progress-bar-circle").forEach((t, r) => {
      const e = t.getAttribute("aria-valuenow"),
        a = Globals[t.getAttribute("data-color")] || Globals.primary,
        s = Globals[t.getAttribute("data-trail-color")] || Globals.separator,
        i = t.getAttribute("aria-valuemax") || 100,
        o = t.getAttribute("data-show-percent"),
        n = t.getAttribute("data-hide-all-text"),
        l = t.getAttribute("data-stroke-width") || 1,
        d = t.getAttribute("data-trail-width") || 1,
        h = parseInt(t.getAttribute("data-duration")) || 20,
        g = t.getAttribute("data-easing") || "easeInOut";
      this._progressBars.push(
        new ProgressBar.Circle(t, {
          color: a,
          duration: h,
          easing: g,
          strokeWidth: l,
          trailColor: s,
          trailWidth: d,
          val: e,
          max: i,
          text: { autoStyleContainer: !1 },
          step: function (t, r) {
            "false" === n &&
              ("true" === o
                ? r.setText(Math.round(100 * r.value()) + "%")
                : r.setText(e + "/" + i));
          },
        })
      );
    });
    for (let t = 0; t < this._progressBars.length; t++)
      this._progressBars[t].animate(
        this._progressBars[t]._opts.val / this._progressBars[t]._opts.max
      );
  }
  _initEvents() {
    document.documentElement.addEventListener(
      Globals.colorAttributeChange,
      (t) => {
        this._streamingLineChart && this._streamingLineChart.destroy(),
          this._initStreamingLineChart(),
          this._streamingBarChart && this._streamingBarChart.destroy(),
          this._initStreamingBarChart(),
          this._progressCircleUpdate();
      }
    );
  }
}
