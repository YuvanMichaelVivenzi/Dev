//
//  ContentView.swift
//  apple walkthrough
//
//  Created by Yuvan Michael Vivenzi on 29/09/25.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Image(systemName: "globe")
                .font(.system(size: 36))
                .imageScale(.large)
                .foregroundStyle(.tint)
            Text("Hello! Let's start doing stuff in Xcode! Making our first macOS app is fun")
        }
        .padding()
    }
}

#Preview {
    ContentView()
}
