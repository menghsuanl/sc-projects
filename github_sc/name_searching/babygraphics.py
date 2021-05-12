"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    inner_width = width - GRAPH_MARGIN_SIZE*2
    # Width between year and year
    width_bw_yr = inner_width/len(YEARS)
    return GRAPH_MARGIN_SIZE + year_index * width_bw_yr


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(0, GRAPH_MARGIN_SIZE, CANVAS_WIDTH, GRAPH_MARGIN_SIZE)
    canvas.create_line(0, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    # Add line for each year
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0,
                           get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
    # Add text
    for i in range(len(YEARS)):
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    inner_height = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2
    # y_base: the height to be moved per rank
    y_base = inner_height/1000
    for i in range(len(lookup_names)):
        y_lst = []
        rank_text_lst = []
        lookup_name = lookup_names[i]
        color = COLORS[i % len(COLORS)]
        for year in YEARS:
            year = str(year)
            # Check if the year exists
            if year in name_data[lookup_name]:
                rank = int(name_data[lookup_name][year])
                rank_text = str(rank)
            # If the year does not exit, means the rank is above 1000
            else:
                rank = 1000
                rank_text = '*'
            # Save ranks, and text to show of each year
            y_lst.append(rank)
            rank_text_lst.append(rank_text)
        for j in range(len(YEARS)-1):
            y1 = y_lst[j]*y_base+GRAPH_MARGIN_SIZE
            y2 = y_lst[j+1]*y_base+GRAPH_MARGIN_SIZE
            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j), y1, get_x_coordinate(CANVAS_WIDTH, j+1), y2,
                               width=LINE_WIDTH, fill=color)
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j+1)+TEXT_DX, y2,
                               text=lookup_name+''+rank_text_lst[j+1], anchor=tkinter.NW)
        # Add text for the first year
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 0)+TEXT_DX, y_lst[0]*y_base+GRAPH_MARGIN_SIZE,
                           text=lookup_name + '' + rank_text_lst[0], anchor=tkinter.NW)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
