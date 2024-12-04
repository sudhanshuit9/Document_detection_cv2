import cv2

from Scanner import detect_and_warp_document


def run_document_scanner():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame. Exiting...")
            break

        # Detect and warp the document
        scanned_document, detected, contour = detect_and_warp_document(frame)

        if detected:
            # Draw bounding box around detected document
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
            cv2.putText(frame, "Document Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Align the document within the frame.", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Display the webcam feed
        cv2.imshow("Document Scanner", frame)

        # If a document is detected, show the scanned version in another window
        if detected:
            cv2.imshow("Scanned Document", scanned_document)

        # Key bindings
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # Quit
            break
        elif key == ord('s') and detected:  # Save the scanned document
            cv2.imwrite("scanned_document.jpg", scanned_document)
            print("Document saved as 'scanned_document.jpg'")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_document_scanner()
