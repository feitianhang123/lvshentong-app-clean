package com.lvshentong.app;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android�?webkit.WebViewClient;

public class MainActivity extends Activity {
    
    private WebView webView;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        webView = findViewById(R.id.webview);
        
        // Enable JavaScript and configure WebView
        WebSettings webSettings = webView.getSettings();
        webSettings.setJavaScriptEnabled(true);�?        webSettings.setDomStorageEnabled(true);
        webSettings.setAllowFileAccess(true);
        webSettings.setAllowContentAccess(true);
        webSettings.setAllowFileAccessFromFileURLs(true);
        webSettings.setAllowUniversalAccessFromFileURLs(true);
        webSettings.setDatabaseEnabled(true);
        
        // 重要：启用混合内容模式，允许HTTPS页面加载HTTP资源
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.LOLLIPOP) {
            webSettings.setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW);
        }
        
        // Set WebView client
        webView.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                // Handle internal links
                if (url.startsWith("file:///")) {
                    view.loadUrl(url);
                    return true;
                }
                // Handle download links
                if (url.endsWith(".doc") || url.endsWith(".docx") || url.endsWith(".pdf") || url.endsWith(".xlsx")) {
                    // Use browser to handle downloads
                    Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
                    startActivity(intent);
                    return true;
                }
                return false;
            }
        });
        
        // Load local HTML file
        webView.loadUrl("file:///android_asset/www/module1_debug.html");
    }
    
    @Override
    public void onBackPressed() {
        if (webView.can极GoBack()) {
            webView.goBack();
        } else {
            super.onBackPressed();
        }
    }
}
