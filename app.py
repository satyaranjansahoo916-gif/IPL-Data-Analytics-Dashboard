import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

# ---------------- LOAD DATA ----------------
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

matches["winner"] = matches["winner"].fillna("No Result")
matches["season"] = matches["season"].astype(str)

# ---------------- THEME ----------------
BG = "#0B1020"
CARD = "#151D32"
TEXT = "#F4F7FC"
MUTED = "#A9B5CC"
BLUE = "#3B82F6"
ORANGE = "#F59E0B"
GREEN = "#10B981"
PINK = "#EC4899"

app = Dash(__name__)
app.title = "IPL Analytics Dashboard"

seasons = sorted(matches["season"].unique())
teams = sorted(
    set(matches["team1"].dropna().unique())
    | set(matches["team2"].dropna().unique())
)

# ---------------- HELPERS ----------------
def card_style():
    return {
        "backgroundColor": CARD,
        "padding": "20px",
        "borderRadius": "14px",
        "boxShadow": "0 4px 14px rgba(0,0,0,0.2)",
        "flex": "1",
        "minWidth": "160px",
    }

def style_figure(fig):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=CARD,
        plot_bgcolor=CARD,
        font=dict(color=TEXT, family="Arial"),
        margin=dict(l=35, r=20, t=65, b=55),
        title_font=dict(size=18),
        legend=dict(font=dict(color=TEXT)),
    )
    fig.update_xaxes(gridcolor="#29334B")
    fig.update_yaxes(gridcolor="#29334B")
    return fig

# ---------------- LAYOUT ----------------
app.layout = html.Div(
    style={
        "backgroundColor": BG,
        "color": TEXT,
        "minHeight": "100vh",
        "padding": "26px",
        "fontFamily": "Arial, sans-serif",
    },
    children=[
        html.Div([
            html.H1(
                "🏏 IPL DATA ANALYTICS",
                style={"marginBottom": "6px", "fontSize": "34px"}
            ),
            html.P(
                "Interactive Cricket Performance & Season Insights",
                style={"color": MUTED, "fontSize": "16px"}
            ),
        ]),

        html.Div([
            html.Div([
                html.Label("📅 Select Season"),
                dcc.Dropdown(
                    id="season-filter",
                    options=[{"label": "All Seasons", "value": "All"}]
                    + [{"label": s, "value": s} for s in seasons],
                    value="All",
                    clearable=False,
                ),
            ], style={"flex": "1", "minWidth": "220px"}),

            html.Div([
                html.Label("🏆 Select Team"),
                dcc.Dropdown(
                    id="team-filter",
                    options=[{"label": "All Teams", "value": "All"}]
                    + [{"label": t, "value": t} for t in teams],
                    value="All",
                    clearable=False,
                ),
            ], style={"flex": "1", "minWidth": "220px"}),
        ], style={
            "display": "flex",
            "gap": "20px",
            "flexWrap": "wrap",
            "margin": "22px 0",
            "backgroundColor": CARD,
            "padding": "20px",
            "borderRadius": "14px",
        }),

        html.Div(
            id="summary",
            style={"color": MUTED, "marginBottom": "15px"}
        ),

        html.Div([
            html.Div([
                html.P("TOTAL MATCHES", style={"color": MUTED}),
                html.H2(id="kpi-matches", children="—"),
            ], style=card_style()),

            html.Div([
                html.P("TEAMS IN DATA", style={"color": MUTED}),
                html.H2(id="kpi-teams", children="—"),
            ], style=card_style()),

            html.Div([
                html.P("SEASONS", style={"color": MUTED}),
                html.H2(id="kpi-seasons", children="—"),
            ], style=card_style()),

            html.Div([
                html.P("TOTAL RUNS", style={"color": MUTED}),
                html.H2(id="kpi-runs", children="—"),
            ], style=card_style()),
        ], style={
            "display": "flex",
            "gap": "16px",
            "flexWrap": "wrap",
            "marginBottom": "24px",
        }),

        html.Div([
            html.Div(dcc.Graph(id="wins-chart"), style=card_style()),
            html.Div(dcc.Graph(id="batsmen-chart"), style=card_style()),
        ], style={
            "display": "grid",
            "gridTemplateColumns": "repeat(auto-fit, minmax(320px, 1fr))",
            "gap": "18px",
            "marginBottom": "18px",
        }),

        html.Div([
            html.Div(dcc.Graph(id="season-chart"), style=card_style()),
            html.Div(dcc.Graph(id="bowlers-chart"), style=card_style()),
        ], style={
            "display": "grid",
            "gridTemplateColumns": "repeat(auto-fit, minmax(320px, 1fr))",
            "gap": "18px",
            "marginBottom": "18px",
        }),

        html.Div([
            html.Div(dcc.Graph(id="toss-chart"), style=card_style()),
            html.Div(dcc.Graph(id="comparison-chart"), style=card_style()),
        ], style={
            "display": "grid",
            "gridTemplateColumns": "repeat(auto-fit, minmax(320px, 1fr))",
            "gap": "18px",
        }),

        html.P(
            "DAVP Project | IPL Data Analysis using Python, Pandas, Plotly & Dash",
            style={
                "textAlign": "center",
                "color": MUTED,
                "marginTop": "30px",
                "padding": "18px",
            },
        ),
    ],
)

# ---------------- DASHBOARD CALLBACK ----------------
@app.callback(
    Output("summary", "children"),
    Output("kpi-matches", "children"),
    Output("kpi-teams", "children"),
    Output("kpi-seasons", "children"),
    Output("kpi-runs", "children"),
    Output("wins-chart", "figure"),
    Output("batsmen-chart", "figure"),
    Output("season-chart", "figure"),
    Output("bowlers-chart", "figure"),
    Output("toss-chart", "figure"),
    Output("comparison-chart", "figure"),
    Input("season-filter", "value"),
    Input("team-filter", "value"),
)
def update_dashboard(selected_season, selected_team):
    filtered = matches.copy()

    if selected_season != "All":
        filtered = filtered[filtered["season"] == selected_season]

    if selected_team != "All":
        filtered = filtered[
            (filtered["team1"] == selected_team)
            | (filtered["team2"] == selected_team)
        ]

    match_ids = filtered["id"].tolist()

    # Filter deliveries for selected matches
    delivery_data = deliveries[
        deliveries["match_id"].isin(match_ids)
    ].copy()

    if selected_team != "All":
        delivery_data = delivery_data[
            delivery_data["batting_team"].eq(selected_team)
            | delivery_data["bowling_team"].eq(selected_team)
        ]

    # KPI calculations
    total_matches = len(filtered)
    total_teams = len(teams)
    total_seasons = filtered["season"].nunique()
    total_runs = int(
        deliveries[deliveries["match_id"].isin(match_ids)]["total_runs"].sum()
    )

    summary = (
        f"Showing {total_matches:,} matches | "
        f"Season: {selected_season} | Team: {selected_team}"
    )

    # 1. Team wins
    wins = (
        filtered[filtered["winner"] != "No Result"]["winner"]
        .value_counts()
        .rename_axis("Team")
        .reset_index(name="Wins")
    )

    wins_fig = px.bar(
        wins, x="Team", y="Wins",
        title="Team Wins",
        color="Wins",
        color_continuous_scale="Blues",
    )
    style_figure(wins_fig)

    # 2. Top batsmen
    batsmen = (
        delivery_data.groupby("batter")["batsman_runs"]
        .sum()
        .nlargest(10)
        .rename_axis("Batsman")
        .reset_index(name="Runs")
    )

    batsmen_fig = px.bar(
        batsmen, x="Batsman", y="Runs",
        title="Top 10 Batsmen by Runs",
        color="Runs",
        color_continuous_scale="Oranges",
    )
    style_figure(batsmen_fig)

    # 3. Matches by season
    season_counts = (
        filtered.groupby("season")
        .size()
        .reset_index(name="Matches")
        .sort_values("season")
    )

    season_fig = px.line(
        season_counts, x="season", y="Matches",
        markers=True, title="Matches by Season",
    )
    season_fig.update_traces(line=dict(color=GREEN, width=3))
    style_figure(season_fig)

    # 4. Top bowlers by wickets
    valid_dismissals = [
        "caught", "bowled", "lbw", "stumped",
        "caught and bowled", "hit wicket"
    ]

    wickets_data = delivery_data[
        (delivery_data["is_wicket"] == 1)
        & (delivery_data["dismissal_kind"].isin(valid_dismissals))
    ]

    bowlers = (
        wickets_data.groupby("bowler")
        .size()
        .nlargest(10)
        .rename_axis("Bowler")
        .reset_index(name="Wickets")
    )

    bowlers_fig = px.bar(
        bowlers, x="Bowler", y="Wickets",
        title="Top 10 Bowlers by Wickets",
        color="Wickets",
        color_continuous_scale="Greens",
    )
    style_figure(bowlers_fig)

    # 5. Toss winner vs match winner
    toss_data = filtered[
        filtered["winner"] != "No Result"
    ].copy()

    toss_data["Outcome"] = (
        toss_data["toss_winner"] == toss_data["winner"]
    ).map({
        True: "Toss winner won match",
        False: "Toss winner lost match",
    })

    toss_summary = (
        toss_data["Outcome"]
        .value_counts()
        .rename_axis("Outcome")
        .reset_index(name="Matches")
    )

    toss_fig = px.bar(
        toss_summary, x="Outcome", y="Matches",
        title="Toss Winner vs Match Winner",
        color="Outcome",
        color_discrete_sequence=[BLUE, PINK],
    )
    style_figure(toss_fig)

    # 6. Team performance comparison
    comparison = (
        filtered[filtered["winner"] != "No Result"]["winner"]
        .value_counts()
        .head(10)
        .rename_axis("Team")
        .reset_index(name="Wins")
    )

    comparison_fig = px.bar(
        comparison, x="Team", y="Wins",
        title="Top 10 Teams: Win Comparison",
        color="Wins",
        color_continuous_scale="Viridis",
    )
    style_figure(comparison_fig)

    return (
        summary,
        f"{total_matches:,}",
        str(total_teams),
        str(total_seasons),
        f"{total_runs:,}",
        wins_fig,
        batsmen_fig,
        season_fig,
        bowlers_fig,
        toss_fig,
        comparison_fig,
    )


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8050)
