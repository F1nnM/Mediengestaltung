import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#st.set_page_config(layout="wide")
with st.expander("Show/Hide Data Input", expanded=True):
    data = pd.DataFrame([
    {
        "Bundesland": country,
        "Bartwuchs": bart,
        "Anzahl": col.slider(f"{country} {bart}", 0, 10),
    }
    for bart in ["Bart", "Bartlos"] for country,col in zip(["Bayern", "BW", "Hessen", "NRW"], st.columns(4))])
    st.session_state.data = data

data = st.session_state.data

for country in ["Bayern", "BW", "Hessen", "NRW"]:
    sum = data[data["Bundesland"] == country]["Anzahl"].sum()
    data.loc[data["Bundesland"] == country, "Bundesland"] = f"{country} ({sum})"

for bart in ["Bart", "Bartlos"]:
    sum = data[data["Bartwuchs"] == bart]["Anzahl"].sum()
    data.loc[data["Bartwuchs"] == bart, "Bartwuchs"] = f"{bart} ({sum})"

# generate plotly scatterplot. X is the country, Y is the Bart/Bartlos category, size is the value
fig = px.scatter(data,
    x="Bartwuchs",
    y="Bundesland",
    size="Anzahl",
    color="Anzahl",
    opacity=1,
    title="Bartwuchs nach Bundesland",
    color_continuous_scale="RdBu")
fig.update_layout(height=450)
fig.update_layout(
    margin=dict(r=430),
    font=dict(
        size=16,
    )
)

"""
# Lorem Ipsum dolor
Sit amet, consectetur adipiscing elit. Curabitur quis efficitur enim, eu feugiat massa. Vestibulum a ex leo. Nulla velit nunc, sollicitudin vel facilisis eu, sagittis in metus. Vestibulum id erat ut enim laoreet porta. Mauris eget congue massa. 
"""
with st.expander("Proin sollicitudin ut ligula at pretium. Sed sit amet tempor dui."):
    """
    ## Nulla aliquam semper nulla id placerat
    Maecenas convallis consectetur mauris, sagittis condimentum neque vestibulum at. Etiam ut commodo nibh, vel ullamcorper risus. Ut dui urna, bibendum ut ante ut, dignissim congue lorem.
    1. Cras convallis mauris sed odio interdum, eget fermentum dui cursus.
    1. Vestibulum posuere, lacus pellentesque viverra tristique. 
    1. Ex risus interdum mauris, sed placerat lorem nisi at odio.
    
    ## Phasellus nec lacus non arcu faucibu
    Pretium quis at dolor. Aenean massa felis, aliquet quis augue non, egestas aliquet quam. Cras vitae diam faucibus metus cursus luctus sed sed est. Fusce elementum justo at egestas feugiat. Maecenas et consectetur lacus. Mauris nec arcu egestas, tempus est eu, ullamcorper lectus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque a dapibus tellus. Phasellus in dui at sapien posuere gravida. Proin at luctus diam.
    """
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig)
with col2:
    """
    ### Mauris quis arcu quam.
    Mauris a turpis sit amet risus hendrerit vulputate. Vestibulum ultricies nulla et ligula facilisis scelerisque. Suspendisse odio turpis, dictum vel orci eu, dignissim tempor nibh.
    - Suspendisse hendrerit arcu magna.
    - Donec non varius leo. Curabitur eget purus orci.
    - Curabitur quis est quis arcu volutpat euismod. Cras at iaculis nunc.
    """

st.sidebar.write("""
# Sidebar infos
## Quisque sollicitudin luctus erat nec auctor.
Donec porta est quis porta aliquet. In efficitur enim at velit iaculis, at laoreet elit interdum.
 - Morbi rutrum tortor ac risus finibus pellentesque.
 - Sed placerat a massa pulvinar ullamcorper.
 - Nullam pellentesque quam nisi, nec elementum lacus varius vel.
Phasellus condimentum enim ac urna interdum, in ullamcorper sapien ullamcorper. 

## Nunc aliquam, ipsum sit.
Amet ornare congue, risus felis pulvinar magna, id hendrerit ligula lorem et sapien.
""")

"""
## Nulla dignissim laoreet vehicula
### Maecenas sollicitudin condimentum aliquet
Mauris luctus id erat quis tempus. Donec pretium, quam et sollicitudin iaculis, nisl orci pellentesque dolor, nec sagittis lacus sapien a arcu. Donec aliquam pulvinar nisl, ut ultricies leo sagittis non.
Nulla dignissim laoreet vehicula. Maecenas sollicitudin condimentum aliquet. Mauris luctus id erat quis tempus. Donec pretium, quam et sollicitudin iaculis, nisl orci pellentesque dolor, nec sagittis lacus sapien a arcu.
### Praesent eget elementum eros
Cras ultricies tincidunt orci a placerat. Praesent venenatis ipsum sit amet quam condimentum, vel dignissim mi dignissim. Nam pulvinar in nibh sed ullamcorper.


"""