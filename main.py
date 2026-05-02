from src.data_loader import load_race_data
from src.visualization import plot_tire_strategy, plot_position_changes
from src.strategy_analysis import detect_undercut
from src.export_data import export_laps_to_csv, export_strategy_summary


def main():
    year = 2023
    gp = 'Monaco'
    session_type = 'R'

    driver1 = 'ALO'
    driver2 = 'HAM'

    print("📥 Loading race data...")
    session, laps = load_race_data(year, gp, session_type)

    print("✅ Data Loaded!")

    # Plots
    plot_tire_strategy(laps, driver1)
    plot_tire_strategy(laps, driver2)
    plot_position_changes(laps, driver1, driver2)

    # Strategy analysis
    detect_undercut(laps, driver1, driver2)

    # ✅ EXPORT (IMPORTANT)
    print("\n💾 Exporting data for Power BI...")
    export_laps_to_csv(laps)
    export_strategy_summary(laps)


if __name__ == "__main__":
    main()