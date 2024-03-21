from folium.features import GeoJsonTooltip
import geopandas as gpd
import folium.plugins
import pandas as pd
import folium as f


def draw_map(tls, data_geojson, cols, aliases, df, lefton, lyrname, keyon, fcolor, lgname, nfcolor, higlt):
    center = [35.762887, 84.083132]
    mapa = f.Map(location=center, zoom_start=1.6,
                 min_zoom=1, max_bounds=True,
                 min_lat=-84, min_lon=-175,
                 max_lat=84,  max_lon=187,
                 control_scale=True,
                 tiles=tls  # cartodb positron
                 )

    # Assuming that data_geojson is a dictionary containing the GeoJSON data
    gpd_geo = gpd.GeoDataFrame.from_features(data_geojson)

    lcol, rcol = cols
    xalias, yalias = aliases

    # Merge the GeoJSON data with df
    gpd_geo = gpd_geo.merge(df, left_on=lefton, right_on=lcol)

    # Create a Choropleth layer with the merged data
    choropleth = f.Choropleth(
        geo_data=gpd_geo.__geo_interface__,
        name=lyrname,
        data=df,
        columns=[lcol, rcol],
        key_on=keyon,
        fill_color=fcolor,
        fill_opacity=0.7,
        line_opacity=0.1,
        legend_name=lgname,
        nan_fill_color=nfcolor,
        line_color="#0000",
        reset=True,
        highlight=higlt,
    ).add_to(mapa)

    # Add tooltips to the Choropleth layer
    choropleth.geojson.add_child(
        GeoJsonTooltip(fields=[lcol, rcol],
                       aliases=[f'{xalias}: ', f'{yalias}: '],
                       labels=True,
                       localize=True,
                       sticky=False)
    )

    f.plugins.Fullscreen(
        position="topright",
        title="Expand me",
        title_cancel="Exit me",
        force_separate_button=True,
    ).add_to(mapa)

    f.LayerControl().add_to(mapa)

    return mapa
