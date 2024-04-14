import streamlit as st
from PIL import Image
import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
import plotly.express as px

def setting_background():


    icon=Image.open(r'C:\Users\Good Day\Desktop\Project-4\airbnb.png')
    st.set_page_config(page_title= "Airbnb Data Visualization",
                    page_icon= icon,
                    layout= "wide",
                    initial_sidebar_state= "expanded",
                    menu_items={'About': """# This dashboard app is created by *Natarajan*!
                                            Data has been gathered from mongodb atlas"""}
                    )
    
    setting_background()

# Giving page Title 
st.markdown("<span style='color: blue; font-size : 50px; font-weight : bold;'>Airbnb Analysis</span>", unsafe_allow_html=True)

# Defining the Menu options in sidebar
selected_option=st.sidebar.radio('Select your option',('**Home**', '**EDA-Visualization**','**User Input**'))

# defining the CSV file as input
df = pd.read_csv(r'C:\Users\Good Day\Desktop\Project-4\Airbnb_data.csv')

if selected_option=='**Home**':
    st.markdown(("## :violet[Home]"))
    col1,col2=st.columns(2)

    with col1:
        st.markdown(("## :blue[Domain] : Travel Industry, Property Management and Tourism"))
        st.image(r"C:\Users\Good Day\Desktop\Project-4\airbnb_home.jfif")
        st.markdown("## :blue[Technologies used] : Python, Pandas, Plotly, Streamlit, MongoDB.")
        

    with col2:
        st.markdown("## :blue[Overview] : To analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends. ")

if selected_option=="**EDA-Visualization**":

    st.markdown(("## :violet[Exploratory Data Analysis]"))

    
    # showing Geomap with mean price wrt countries
    price = df.groupby('Country')['Price'].mean().reset_index()

    col1,col2=st.columns(2)

    with col1:

        fig = px.scatter_geo(price, locations="Country", 
                            locationmode='country names',
                            color="Price",
                            hover_name="Country",
                            size="Price",
                            color_continuous_scale='viridis',
                            title="Average Airbnb Prices by Country")
        fig.update_layout(width=600)
        st.write(fig, use_container_width=True)

    with col2:

        # Listing Price in each country
        fig_1 = px.scatter(data_frame=df,
            x='Country',y='Price',
            color='Country',
            size='Price',
            opacity=0.5,
            size_max=50,
            title='Listing Price in each Countries')
        
        fig_1.update_layout(showlegend=False)
        st.plotly_chart(fig_1, use_container_width=True)


    # options=st.radio("**Choose one option**", [":rainbow[Country Wise Listings]", ":blue[Top 10 Properties]", ":rainbow[Room Type]", ":blue[Bed Type]"])

    # if options==":rainbow[Country Wise Listings]":
    cola,colb=st.columns(2)
    with cola:

        # Calculate the list of countries
        country_list_count=df['Country'].value_counts()
        # Define colors for each bar
        colors = ['blue', 'green', 'red', 'orange', 'purple', 'yellow']

        # Plotting the bar plot
        property=px.bar(x=country_list_count.index, y=country_list_count.values, color=country_list_count.index,
                        title="Number of Listings in each Country", labels={'x':'Country', 'y':'No of Listings'}, text_auto=True)
        

        property.update_traces(text=country_list_count.values, textposition= 'inside')
        property.update_layout(width=600, height=500, xaxis=dict(showgrid=False), yaxis=dict(showgrid=False), showlegend=False)
        
        st.plotly_chart(property, use_container_width=True)
        

               
        # plt.figure(figsize=(10, 8))
        # plt.figure(facecolor='white')
        # bars=plt.bar(country_list_count.index, country_list_count.values, align='center', alpha=0.5, color=colors, width=0.5)
        # plt.title('Number of Listings in Each Country')
        # plt.xlabel('Country')
        # plt.ylabel('Number of Listings')

        # # Adding bar values on top of each bar
        # for bar in bars:
        #     height = bar.get_height()
        #     plt.text(bar.get_x() + bar.get_width() / 2, height, height, ha='center', va='bottom', fontsize=10)
        # # Rotating x-axis labels to 45 degrees
        # plt.xticks(rotation=45)
        # st.pyplot(plt.gcf())

        
    # if options==":blue[Top 10 Properties]":

    with colb:
        
        
        # Top 10 Property_type Listings
        property_counts = df['Property_type'].value_counts()

        top_10_property_type=property_counts.head(10)

        
        ax=px.bar(x=top_10_property_type.index,y=top_10_property_type.values, color=top_10_property_type.index,
                title='Top 10 Property Type Listings', labels={'x': 'Property Type', 'y':'Count'}, text_auto=True)
        ax.update_traces(text=property_counts , textposition='inside')
        
        ax.update_layout(width=600, height=500, xaxis=dict(showgrid=False), yaxis=dict(showgrid=False), showlegend=False)
        
        st.plotly_chart(ax, use_container_width=True)
            

    # if options== ":rainbow[Room Type]":

    colc,cold=st.columns(2)

    with colc:

        # Listing in Each Room type
        # Calculate the count of listings for each room type
        room_type_counts=df['Room_type'].value_counts()

        room_type_df=pd.DataFrame({'Room_type':room_type_counts.index, 'Count': room_type_counts.values})

        # Update layout to adjust chart size
        fig.update_layout(width=600, height=500)

        # Create a pie chart using Plotly Express
        fig=px.pie(room_type_df, values='Count', names="Room_type", title='Number of Listing in each Room type')
        fig.update_traces(textinfo='label+percent', textposition='outside', hoverinfo= 'label+percent')
        fig.update_layout(showlegend=False)

        st.plotly_chart(fig, use_container_width=True)
    
    # if options==":blue[Bed Type]":

    with cold:

        st.markdown("")
        st.markdown("")

        st.markdown("<b>Number of Listings in Each Bed Type</b>", unsafe_allow_html=True)

        # Types of Beds Available
        bed_type_count=df['Bed_type'].value_counts()
        
        bed_df=pd.DataFrame({'bed_type':bed_type_count.index, 'count': bed_type_count.values})

        # Create a pie chart using Plotly Express
        fig=px.sunburst(bed_df, path=['bed_type', 'count'], values= bed_type_count.values, custom_data=['bed_type'])

        # Customize hover template to display 'bed_type' next to count
        fig.update_traces(hovertemplate='<b>Bed Type</b>: %{customdata[0]}<br><b>Count</b>: %{value}')

            # Update layout to adjust chart size
        fig.update_layout(width=600, height=420)
        

        st.plotly_chart(fig,use_container_width=True)

countries=df['Country'].unique()
property=df['Property_type'].unique()
room=df['Room_type'].unique()
# available=df[['Availability_30'], df['Availability_60'], df['Availability_90'], df['Availability_365']]

if selected_option=='**User Input**':
    # st.image(r"C:\Users\Good Day\Desktop\Project-4\airbnb.png")
    
    st.markdown(":blue[**Exploring Listings by User Input**]")



    col1, col2=st.columns(2)

    with col1:
        st.markdown("")
        st.markdown("")

        with st.container(border=True):
        
            cola,colb=st.columns(2)

            with cola:

                selected_countries=st.multiselect("Select list of Countries:", countries)
            
            with colb:
                
                selected_property=st.multiselect("Select Your Property Type:", property)
            
            colc,cold=st.columns(2)

            with colc:
            
                selected_room=st.multiselect("Select your Room Type:", room)
            
            # price=st.slider("Choose Your Price Range:",  min_value=df['Price'].min(), max_value=df['Price'].max())

            with cold:
                

                # Input fields for the minimum and maximum values of the range
                min_value = st.number_input('Min Price :', value=df['Price'].min())
            
                max_value = st.number_input('Max Price:', value=df['Price'].max())

    with col2:   
        # Filter the DataFrame based on the selected price range
        filtered_df = df[(df['Country'].isin(selected_countries)) &
                        (df['Property_type'].isin(selected_property)) & 
                        (df['Room_type'].isin(selected_room)) &
                        (df["Price"]>=min_value ) &
                        (df["Price"]<=max_value)
                        ]

        
        # Group by country and room type to get counts
        room_type_counts = filtered_df.groupby(["Country", "Room_type"]).size().reset_index(name='Count')

        # Create a pivot table to prepare data for grouped bar chart
        pivot_df = room_type_counts.pivot(index='Country', columns='Room_type', values='Count').fillna(0)

        # Stack the room types for each country
        pivot_df = pivot_df.stack().reset_index(name='Count')

        if selected_countries and selected_property and selected_room:

            # Create bar chart
            result = px.bar(pivot_df, x="Country", y="Count", color="Room_type",
                        title="Total Listings for User Input",
                        labels={"Count": "Number of Listings"},
                        barmode='group', text_auto=True)

            # Update layout
            result.update_layout(xaxis=dict(title='Country', showgrid=False), yaxis=dict(title='Number of Listings', showgrid=False),
                                 width=400,height=400, showlegend=True)
            

            # Show the plot
            st.plotly_chart(result, use_container_width=True)

    colx1,coly1=st.columns(2)

    

    with colx1:

        # to align
        st.markdown(" ")
        st.markdown(" ")


        with st.container(border=True):
        
            cola1,colb1=st.columns(2)

            with cola1:

                avail_countries=st.multiselect("Select list of Countries:", countries, key="countries_multiselect")
            
            with colb1:
                        
                avail_property=st.multiselect("Select Your Property Type:", property, key="property_multiselect")
            
            colc1,cold1=st.columns(2)

            with colc1:
            
                avail_room=st.multiselect("Select your Room Type:", room,key="room_multiselect")

            with cold1:

                
                # Input fields for Season
                options=st.selectbox("Choose Your Season:", ["Season 1", "Season 2", "Season 3", "Season 4"])
                # st.radio("Choose One Season", 'Season 1', 'Season 2', 'Season 3', 'Season 4')
    with coly1:


        availability_30 =df.groupby('Country')["Availability_30"].mean().reset_index()
        availability_60 =df.groupby('Country')["Availability_60"].mean().reset_index()
        availability_90 =df.groupby('Country')["Availability_90"].mean().reset_index()
        availability_365=df.groupby('Country')["Availability_365"].mean().reset_index()

        # Create Dataframe for Season based on options selected

        # option_df=df[(df['Country'].isin(avail_countries)) &
        #                 (df['Property_type'].isin(avail_property)) &
        #                 (df['Room_type'].isin(avail_room)) &
        #                 (df['Availability_30']) &
        #                 (df['Availability_60']) &
        #                 (df['Availability_90']) &
        #                 (df['Availability_365'])]

        option_df=df[(df['Country'].isin(avail_countries)) &
                        (df['Property_type'].isin(avail_property)) &
                        (df['Room_type'].isin(avail_room))]
      


        
        merged_df=pd.merge(option_df, availability_30, on='Country', how='inner')
        merged_df1=pd.merge(option_df, availability_60, on='Country', how='inner')
        merged_df2=pd.merge(option_df, availability_90, on='Country', how='inner')
        merged_df3=pd.merge(option_df, availability_365, on='Country', how='inner')

        

        if avail_countries and avail_property and avail_room and options=="Season 1":

            # st.markdown(":blue[**Season=Availability_30**]")

            # res=px.line_3d(df, x= availability_30, y=df['Country'].value_counts(), color= "Country",  hover_name="Country")
            

            # Assuming availability_30 is a column name in your DataFrame df
            res = px.bar(merged_df, x='Country', y='Availability_30_x',title="Listing Available Pattern- Availability_30", color="Country", hover_name="Availability_30_y",
                         labels={"Availability_30_y": "No. of days Available"})
            # Update layout
            res.update_layout(xaxis=dict(title='Country', showgrid=False), yaxis=dict(title='No. of days Listings Available', showgrid=False),
                                 width=400,height=400, showlegend=True)
            st.plotly_chart(res, use_container_width=True)

            # res = px.scatter_geo(merged_df, locations="Country", 
            #                 locationmode='country names',
            #                 color="Availability_30_x",
            #                 hover_name="Country",
            #                 size= 'Availability_30_x',
            #                 color_continuous_scale='viridis',
            #                 title="Average Airbnb Prices by Country")
            # res.update_layout(width=600)
            # st.plotly_chart(res, use_container_width=True)
            # st.write(option_df)
        
        elif avail_countries and avail_property and avail_room and options=="Season 2":

            # st.markdown(":blue[**Season=Availability_60**]")

            
            # Assuming availability_30 is a column name in your DataFrame df
            res = px.bar(merged_df1, x='Country', y='Availability_60_x',title="Listing Available Pattern- Availability_60", color="Country", hover_name="Availability_60_y")
            # Update layout
            res.update_layout(xaxis=dict(title='Country', showgrid=False), yaxis=dict(title='No. of days Listings Available', showgrid=False),
                                 width=400,height=400, showlegend=True)
            st.plotly_chart(res, use_container_width=True)

        elif avail_countries and avail_property and avail_room and options=="Season 3":

            # st.markdown(":blue[**Season=Availability_90**]")

            
            # Assuming availability_30 is a column name in your DataFrame df
            res = px.bar(merged_df2, x='Country', y='Availability_90_x',title="Listing Available Pattern- Availability_90", color="Country", hover_name="Availability_90_y")
            # Update layout
            res.update_layout(xaxis=dict(title='Country', showgrid=False), yaxis=dict(title='No. of days Listings Available', showgrid=False),
                                 width=400,height=400, showlegend=True)
            st.plotly_chart(res, use_container_width=True)

        elif avail_countries and avail_property and avail_room and options=="Season 4":

            # st.markdown(":blue[**Season=Availability_365**]")

            
            # Assuming availability_30 is a column name in your DataFrame df
            res = px.bar(merged_df3, x='Country', y='Availability_365_x',title="Listing Available Pattern- Availability_365", color="Country", hover_name="Availability_365_y")
            # Update layout
            res.update_layout(xaxis=dict(title='Country', showgrid=False), yaxis=dict(title='No. of days Listings Available', showgrid=False),
                                 width=400,height=400, showlegend=True)
            st.plotly_chart(res, use_container_width=True)

        











            







     

                                                        