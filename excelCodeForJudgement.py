import pandas as pd
import os

def AppendParticipantResponseInMainExcelForOurJudgement(name, newRowData):
    # Convert new row to DataFrame
    new_df = pd.DataFrame([newRowData], columns=[
        'Participant1Name', 'Participant2Name', 'ScoreForAll5Questions',
        'Participant - 1 RNo.', 'Participant - 2 RNo.', 'TimeTakenToCompleteThetest'
    ])

    excel_filename = f"{name}.xlsx"

    try:
        if os.path.exists(excel_filename):
            # Read the existing file
            existing_df = pd.read_excel(excel_filename, engine='openpyxl')
            # Append new data
            updated_df = pd.concat([existing_df, new_df], ignore_index=True)
        else:
            return -1
            # If file doesn't exist, start with new_df
            # updated_df = new_df

        # Save back to Excel
        updated_df.to_excel(excel_filename, index=False, engine='openpyxl')
        return 0
    except Exception as e:
        return -1
    return 0
