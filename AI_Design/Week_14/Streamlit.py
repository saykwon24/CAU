"""
Streamlit: python library that facilitates the creation and development of custom web apps
           ideal for supporting data science and ML projects
           using a virtual environment is always recommended (e.g. anaconda)
           
           some examples >>> https://streamlit.io/gallery
           installation  >>> https://docs.streamlit.io/library/get-started/installation
           configuration >>> https://docs.streamlit.io/library/advanced-features/configuration

    Start: enter 'streamlit hello' in anaconda command line, then access the URL
    
    Development
        Rerun: every time with the click, application updates is saved without the need to restart the server
        Always rerun: application updates automatically with no click
    
    Project Structure: directory structure
        need to define an 'entrypoint file' that represents the main page to show to the user
        other additional pages should be placed in a sub-folder 'pages/'
        pages globally share the same Python modules
        pages are defined by files '.py' within 'pages/' folder
        the number used as a prefix in the file name is not interpreted as part of the title
    
    Page Configuration: must be the first streamlit command and set only once
    
    Elements of Streamlit: text, input widgets, layout, visualization of data and graphs, additional elements
    
    Markdown: used to insert formatted strings, and also HTML code
        >>> https://www.markdownguide.org/basic-syntax/

    Write: allows to write in the app
        [syntax] streamlit.write(*args, unsafe_allow_html=False, **kwargs)
    
    Button: allows to show a simple button that can be clicked
        [syntax] streamlit.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, type='seondary', disabled=False, use_container_width=False)
    
    Checkbox: allows to show a checkbox to check
              returns True or False based on checkbox status
        [syntax] streamlit.checkbox(label, value=False, key=None, help=None, args=None, kwargs=None, *, disabled=False, label_visibility='visible')
    
    Radio Button: allows to insert radio button with which user can make an exclusive choice
                  returns the chosen option
        [syntax] streamlit.radio(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, horizontal=False, lable_visibility='visible')
    
    Selection Box: allows to insert a drop-down selection box
                   returns the chosen option
        [syntax] streamlit.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility='visible')
    
    Multiselect: allows to choose multiple alternatives
                 returns the list of selected options
        [syntax] streamlit.multiselect(label, options, default=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility='visible', max_selections=None)
            default        | speicifies the list of options selected at startup
            max_selections | defines the maximum number of options that can be selected

    Slider: offers a slider that accepts int, float, time, date and datetime
            returns the selected value or tuple for ranges
        [syntax] streamlit.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility='visible')
            min_value | defines the minimum allowable value
                        default = 0 for int, 0.0 for float
            max_value | defines the maximum allowable value
                        default = 100 for int, 1.0 for float
            value     | defines the assumed value for the first time
                        selectable range for tuple, min_value by default
            step      | defines the interval between one value and another
                        default = 1 for int, 0.01 for float

    Text Input: offers the possibility of single-line text input
        [syntax] streamlit.text_input(label, value='', max_chars=None, key=None, type='default', help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility='visible')
    
    Number Input: allows to pass a number from the keyboard or using the '+' and '-' keys
        [syntax] streamlit.number_input(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility='visible')
    
    Form: allows to group several elements on a form or container
          integrated a submit button that collects all the values acquired by the different widgets
        [syntax] streamlit.form(key, clear_on_submit=False)
    
    Dataframe: displays pandas dataframes
        [syntax] streamlit.dataframe(data=None, width=None, height=None, *, use_container_width=False)
    
    ... and so on
"""